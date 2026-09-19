import json
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


if __name__ == "__main__":
    unittest.main()
