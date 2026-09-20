import json
import unittest

from scraper.apply_agent_skills_backfill import add_tag


class AgentSkillsBackfillTest(unittest.TestCase):
    def test_adds_agent_skills_without_replacing_existing_tags(self):
        value, changed = add_tag('["coding", "tools-integrations"]', "agent-skills")

        self.assertTrue(changed)
        self.assertEqual(
            json.loads(value),
            ["coding", "tools-integrations", "agent-skills"],
        )

    def test_existing_agent_skills_tag_is_idempotent(self):
        value, changed = add_tag('["agent-skills", "coding"]', "agent-skills")

        self.assertFalse(changed)
        self.assertEqual(json.loads(value), ["agent-skills", "coding"])

    def test_rejects_non_array_tags(self):
        with self.assertRaisesRegex(ValueError, "JSON string array"):
            add_tag('"coding"', "agent-skills")


if __name__ == "__main__":
    unittest.main()
