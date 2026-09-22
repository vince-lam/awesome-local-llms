import json
import unittest

from scraper import update_stats


class FakeDB:
    def __init__(self, rows):
        self.rows = rows
        self.writes = []

    def query(self, sql):
        return self.rows

    def executemany(self, statements):
        self.writes.extend(statements)


class CategoryBackfillTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy = update_stats.load_taxonomy()

    def test_fills_category_when_all_tags_share_a_parent(self):
        db = FakeDB([["example/repo", json.dumps(["coding", "automation"])]])

        update_stats.backfill_missing_categories(db, self.taxonomy)

        self.assertEqual(len(db.writes), 1)
        self.assertEqual(db.writes[0][1], ["applications", "example/repo"])
        self.assertIn("category IS NULL OR category = ''", db.writes[0][0])

    def test_rejects_cross_category_tags_before_writing(self):
        db = FakeDB([
            ["example/simple", json.dumps(["coding"])],
            ["example/mixed", json.dumps(["coding", "agent-skills"])],
        ])

        with self.assertRaisesRegex(ValueError, "example/mixed"):
            update_stats.backfill_missing_categories(db, self.taxonomy)

        self.assertEqual(db.writes, [])

    def test_rejects_unknown_tags(self):
        db = FakeDB([["example/unknown", json.dumps(["coding", "not-a-tag"])]])

        with self.assertRaisesRegex(ValueError, "example/unknown"):
            update_stats.backfill_missing_categories(db, self.taxonomy)

        self.assertEqual(db.writes, [])


if __name__ == "__main__":
    unittest.main()
