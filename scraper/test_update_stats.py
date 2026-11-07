import json
import re
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from scraper import update_stats


class ReadmeRankingsTest(unittest.TestCase):
    def test_rankings_are_ordered_and_globally_unique(self):
        categories = [
            {"category": "Applications", "slug": "applications"},
            {"category": "Infrastructure", "slug": "infrastructure"},
        ]
        rows = []
        for index in range(50):
            category = categories[index % 2]["category"]
            rows.append({
                "Owner": "owner",
                "Repository Name": f"repo-{index:02d}",
                "Category": category,
                "About": f"Description {index}",
                "URL": f"https://github.com/owner/repo-{index:02d}",
                "_stars": 10_000 - index,
                "_days": 1,
                "_delta_7d": index * 10,
            })
        # Unknown growth may be an established leader, but never a mover.
        rows[0]["_delta_7d"] = None

        with tempfile.TemporaryDirectory() as directory:
            taxonomy = Path(directory) / "categories.json"
            taxonomy.write_text(json.dumps(categories))
            with patch.object(update_stats, "TAXONOMY_FILE", str(taxonomy)):
                markdown = update_stats.build_markdown_table(pd.DataFrame(rows))

        self.assertIn("## Established leaders", markdown)
        self.assertIn("## Trending this week", markdown)
        self.assertIn("## Trending by category", markdown)
        self.assertIn("repo-00", markdown)
        self.assertIn("n/a", markdown)
        self.assertEqual(markdown.count("https://github.com/owner/"), 46)
        for index in range(50):
            url = f"https://github.com/owner/repo-{index:02d}"
            self.assertLessEqual(markdown.count(url), 1)

    def test_growth_label_uses_previous_star_count(self):
        self.assertEqual(update_stats._growth_label(1_100, 100), "+100 (+10.0%)")


class StatsUpdatedAtTest(unittest.TestCase):
    def test_records_and_overwrites_iso_utc_timestamp(self):
        conn = sqlite3.connect(":memory:")

        class FakeDb:
            def execute(self, sql, args=None):
                conn.execute(sql, args or [])

        update_stats.record_stats_updated_at(FakeDb())
        conn.execute("UPDATE site_meta SET value = 'old'")
        update_stats.record_stats_updated_at(FakeDb())

        rows = conn.execute("SELECT key, value FROM site_meta").fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], "stats_updated_at")
        self.assertRegex(rows[0][1], re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"))


class RenameReconciliationTest(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.executescript((Path(__file__).parents[1] / 'db/schema.sql').read_text())
        conn = self.conn

        class Db:
            def query(self, sql, args=None):
                return conn.execute(sql, args or []).fetchall()

            def transaction(self, statements):
                conn.commit()
                with conn:
                    for sql, args in statements:
                        conn.execute(sql, args)

        self.db = Db()

    def add_repo(self, name, tags='[]'):
        owner, repo = name.split('/')
        return self.conn.execute('INSERT INTO repos (full_name, owner, name, url, tags) VALUES (?, ?, ?, ?, ?)', [name, owner, repo, 'https://github.com/' + name, tags]).lastrowid

    def frame(self):
        return pd.DataFrame([
            {'Owner': 'new', 'Repository Name': 'project', '_requested_repo': 'old/project'},
            {'Owner': 'new', 'Repository Name': 'project', '_requested_repo': 'new/project'},
        ])

    def test_merge_preserves_history_and_curated_tags_and_is_idempotent(self):
        old = self.add_repo('old/project', '["old-tag"]')
        new = self.add_repo('new/project', '["new-tag"]')
        self.conn.executemany('INSERT INTO snapshots (repo_id, scraped_date, stars) VALUES (?, ?, ?)', [(old, '2026-01-01', 1), (old, '2026-01-02', 2), (new, '2026-01-02', 3)])
        self.conn.execute("INSERT INTO candidates (full_name, status) VALUES ('old/project', 'accepted')")
        for _ in range(2):
            result = update_stats.reconcile_repository_names(self.db, self.frame())
            self.assertEqual(len(result), 1)
        self.assertEqual(self.db.query('SELECT full_name, tags FROM repos'), [('new/project', '["new-tag", "old-tag"]')])
        self.assertEqual(self.db.query('SELECT repo_id, stars FROM snapshots ORDER BY scraped_date'), [(new, 1), (new, 3)])
        self.assertEqual(self.db.query('SELECT status FROM candidates'), [('duplicate',)])

    def test_rename_without_target_keeps_id_and_history(self):
        old = self.add_repo('old/project')
        update_stats.reconcile_repository_names(self.db, self.frame().iloc[:1])
        self.assertEqual(self.db.query('SELECT id, full_name FROM repos'), [(old, 'new/project')])

    def test_fetch_uses_github_identity_and_retains_each_alias_until_merge(self):
        from unittest.mock import Mock
        response = Mock(ok=True, headers={})
        response.json.return_value = {"data": {
            "r0": {"nameWithOwner": "new/project", "stargazerCount": 42},
            "r1": {"nameWithOwner": "new/project", "stargazerCount": 42},
        }}
        entries = [{"repo": "old/project"}, {"repo": "new/project"}]
        taxonomy = {"subcategories": {}, "categories": {}, "keywords": {}}
        with patch.object(update_stats, "_post", return_value=response):
            frame = update_stats.fetch_all(Mock(), entries, taxonomy)
        self.assertEqual(len(frame), 2)
        self.assertEqual(set(frame['_requested_repo']), {'old/project', 'new/project'})
        self.assertEqual(set(frame['URL']), {'https://github.com/new/project'})
        self.add_repo('old/project')
        self.add_repo('new/project')
        result = update_stats.reconcile_repository_names(self.db, frame)
        self.assertEqual(len(result), 1)
        self.assertEqual(self.db.query('SELECT full_name FROM repos'), [('new/project',)])

    def test_failed_merge_rolls_back_history_and_registry(self):
        old = self.add_repo('old/project')
        self.add_repo('new/project')
        self.conn.execute("INSERT INTO snapshots (repo_id, scraped_date, stars) VALUES (?, '2026-01-01', 1)", [old])
        self.conn.execute("CREATE TRIGGER prevent_delete BEFORE DELETE ON repos BEGIN SELECT RAISE(ABORT, 'test failure'); END")
        with self.assertRaises(sqlite3.IntegrityError):
            update_stats.reconcile_repository_names(self.db, self.frame())
        self.assertEqual(len(self.db.query('SELECT id FROM repos')), 2)
        self.assertEqual(self.db.query('SELECT repo_id FROM snapshots'), [(old,)])

    def test_distinct_forks_are_kept(self):
        self.add_repo('old/project')
        self.add_repo('new/project')
        frame = self.frame()
        frame.loc[0, 'Owner'] = 'old'
        result = update_stats.reconcile_repository_names(self.db, frame)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(self.db.query('SELECT id FROM repos')), 2)


if __name__ == "__main__":
    unittest.main()
