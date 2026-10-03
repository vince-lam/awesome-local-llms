from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from scraper import benchmark_classifiers as base
from scraper import refine_jev_benchmark as refinement


class JevRefinementTest(unittest.TestCase):
    def test_target_reference_is_excluded_from_category_criteria(self):
        refs = [{"name": "target", "description": "unique target description",
                 "classification": {"category": "applications"}},
                {"name": "other", "description": "another application",
                 "classification": {"category": "applications"}}]
        question = refinement.category_question(base.load_taxonomy(), refs, "target")
        criteria = question["category"]["criteria"]["applications"]
        self.assertNotIn("unique target description", criteria)
        self.assertIn("another application", criteria)

    def test_tag_stage_covers_all_roles_and_keywords(self):
        tax = base.load_taxonomy()
        questions = refinement.role_questions(tax)
        self.assertNotIn("category", questions)
        self.assertEqual(len(questions), len(tax.subcategory_slugs) + len(tax.keyword_slugs))

    def test_exhausted_credits_remove_only_confirmed_failed_marker(self):
        response = Mock(status_code=402, url=base.JEV_URL)
        response.json.return_value = {"error": {"message": "Insufficient credits"}}
        with tempfile.TemporaryDirectory() as directory, \
                patch.dict(base.os.environ, {"OPENROUTER_API_KEY": "test-key"}), \
                patch.object(base, "http", side_effect=base.ProviderHTTPError(response)):
            output = Path(directory)
            with self.assertRaises(base.ProviderHTTPError):
                refinement.call("category", {"full_name": "example/repo"}, 0, output, {})
            self.assertFalse((output / "category-000-pending.json").exists())
            self.assertEqual(base.read(output / "category-000-error.json")["http_status"], 402)


if __name__ == "__main__":
    unittest.main()
