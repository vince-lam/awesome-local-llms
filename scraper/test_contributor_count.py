import unittest
from types import SimpleNamespace

from scraper import update_stats


class FakeSession:
    def __init__(self, status_code):
        self.response = SimpleNamespace(status_code=status_code, headers={}, ok=False)

    def get(self, url, params, timeout):
        return self.response


class ContributorCountTest(unittest.TestCase):
    def test_missing_repo_has_unknown_contributor_count(self):
        self.assertEqual(
            update_stats._fetch_one_contributor_count(FakeSession(404), "a/missing"),
            ("a/missing", None),
        )

    def test_empty_repo_has_zero_contributors(self):
        self.assertEqual(
            update_stats._fetch_one_contributor_count(FakeSession(204), "a/empty"),
            ("a/empty", 0),
        )


if __name__ == "__main__":
    unittest.main()
