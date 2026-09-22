import json
import unittest
from pathlib import Path

from scraper.classifier import Taxonomy, build_system_prompt, normalise_result


class AgentSkillsTaxonomyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_dir = Path(__file__).parent / "data"
        categories = json.loads((data_dir / "categories.json").read_text())
        keywords = json.loads((data_dir / "keywords.json").read_text())
        cls.taxonomy = Taxonomy(categories, keywords)

    def test_agent_skills_is_an_ai_engineering_subcategory(self):
        self.assertEqual(
            self.taxonomy.sub_to_cat["agent-skills"],
            "ai-engineering",
        )

    def test_prompt_encodes_agent_skills_boundary_and_domain_distinction(self):
        prompt = build_system_prompt(self.taxonomy)

        self.assertIn("publishing installable Agent Skills", prompt)
        self.assertIn("Excludes tutorials and documentation", prompt)
        self.assertIn("link-only lists", prompt)
        self.assertIn("incidental skill support", prompt)
        self.assertIn("distinct from the Skill artifact kind", prompt)

    def test_agent_skills_can_coexist_with_other_subcategories(self):
        result = normalise_result(
            {
                "category_slug": "applications",
                "subcategory_slugs": ["coding", "agent-skills"],
                "keyword_slugs": [],
                "confidence": 1,
                "reason": "Publishes coding skills.",
            },
            self.taxonomy,
        )

        self.assertEqual(result["category"], "applications")
        self.assertEqual(result["subcategories"], ["coding", "agent-skills"])


if __name__ == "__main__":
    unittest.main()
