"""Exercise the production SQL against SQLite, including NULLs and partial scrapes."""
import os
import sqlite3
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from scraper import update_stats as stats


class UsageOptimisationTest(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.executescript((Path(__file__).parents[1] / "db/schema.sql").read_text())
        self.conn.execute("INSERT INTO repos (id, full_name, owner, name, url) VALUES (1, 'a/one', 'a', 'one', 'https://github.com/a/one')")
        conn = self.conn

        class Db:
            def execute(self, sql, args=None):
                return conn.execute(sql, args or [])

            def executemany(self, statements):
                for sql, args in statements:
                    conn.execute(sql, args)
        self.db = Db()

    def snapshot(self, day, stars=100, license=None):
        self.conn.execute(stats._UPSERT_SNAPSHOT_SQL, [day, stars, 2, 3, 4, 5, 6, license, 'Python', 7, 'a/one'])

    def test_identical_snapshot_rerun_writes_zero_but_corrections_and_new_days_survive(self):
        self.snapshot('2026-11-01')
        before = self.conn.total_changes
        self.snapshot('2026-11-01')
        self.assertEqual(self.conn.total_changes - before, 0)
        self.snapshot('2026-11-01', license='MIT')
        self.snapshot('2026-11-01', license=None)
        self.snapshot('2026-11-02')
        self.assertEqual(self.conn.execute('SELECT scraped_date, license FROM snapshots ORDER BY scraped_date').fetchall(), [('2026-11-01', None), ('2026-11-02', None)])

    def test_metadata_null_transitions_and_noop_writes(self):
        for sql in (stats._UPDATE_DESC_SQL, stats._UPDATE_OWNER_TYPE_SQL):
            for value in (None, '', 'changed', None):
                self.conn.execute(sql, [value, 'a/one', value])
                before = self.conn.total_changes
                self.conn.execute(sql, [value, 'a/one', value])
                self.assertEqual(self.conn.total_changes, before)
        self.assertEqual(self.conn.execute('SELECT description, owner_type FROM repos').fetchone(), (None, None))

    def test_writer_reuses_identical_metadata_and_snapshots(self):
        frame = pd.DataFrame([{'Owner': 'a', 'Repository Name': 'one', 'About': 'Description', 'owner_type': 'Organization', 'Stars': 100, 'Forks': 2, 'Issues': 3, '_days': 1}])
        stats.write_snapshots_to_db(self.db, frame, {'a/one': 7})
        before = self.conn.total_changes
        stats.write_snapshots_to_db(self.db, frame, {'a/one': 7})
        self.assertEqual(self.conn.total_changes, before)
        frame.loc[0, 'About'] = 'No description available'
        stats.write_snapshots_to_db(self.db, frame, {'a/one': 7})
        self.assertEqual(self.conn.execute('SELECT description FROM repos').fetchone(), (None,))

    def test_refresh_matches_history_and_repeated_refresh_writes_zero(self):
        self.snapshot('2026-10-01', 10)
        self.snapshot('2026-10-24', 30)
        self.snapshot('2026-10-30', 80)
        self.snapshot('2026-10-31', 100)
        self.conn.execute("INSERT INTO repos (id, full_name, owner, name, url) VALUES (2, 'a/empty', 'a', 'empty', '')")
        before = self.conn.total_changes
        stats.refresh_denormalized_columns(self.db)
        self.assertEqual(self.conn.total_changes - before, 1)
        self.assertEqual(self.conn.execute('SELECT snapshot_count, latest_stars, delta_1d, delta_7d, delta_30d FROM repos WHERE id=1').fetchone(), (4, 100, 20, 70, 90))
        before = self.conn.total_changes
        stats.refresh_denormalized_columns(self.db)
        self.assertEqual(self.conn.total_changes, before)
        # A partial scrape's older repo still retains its own history, not today's date.
        self.snapshot('2026-11-01', 110)
        stats.refresh_denormalized_columns(self.db)
        self.assertEqual(self.conn.execute('SELECT snapshot_count, latest_scraped_date, delta_1d FROM repos WHERE id=1').fetchone(), (5, '2026-11-01', 10))
        # Same-day correction must refresh the cache, too.
        self.snapshot('2026-11-01', 120)
        stats.refresh_denormalized_columns(self.db)
        self.assertEqual(self.conn.execute('SELECT latest_stars FROM repos WHERE id=1').fetchone(), (120,))


class CacheCallbackTest(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    @patch.object(stats.requests, 'post')
    def test_callback_is_optional(self, post):
        stats.invalidate_website_cache()
        post.assert_not_called()

    @patch.dict(os.environ, {'WEB_REVALIDATE_URL': 'https://llmrepos.com/api/revalidate', 'WEB_REVALIDATE_SECRET': 'test'}, clear=True)
    @patch.object(stats.requests, 'post')
    def test_success_and_failure_are_bounded_and_do_not_fail_the_scrape(self, post):
        post.return_value = Mock(status_code=200)
        post.return_value.json.return_value = {'revalidated': True}
        stats.invalidate_website_cache()
        self.assertEqual(post.call_args.kwargs['timeout'], 15)
        self.assertFalse(post.call_args.kwargs['allow_redirects'])
        post.side_effect = stats.requests.Timeout()
        stats.invalidate_website_cache()
