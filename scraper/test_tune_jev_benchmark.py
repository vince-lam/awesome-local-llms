from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from scraper import benchmark_classifiers as base
from scraper import tune_jev_benchmark as tuning


class JevTuningTest(unittest.TestCase):
    def test_split_is_disjoint_reproducible_and_complete(self):
        labels = {str(i): {"category": str(i % 3)} for i in range(30)}
        training, holdout = tuning.split(labels)
        self.assertEqual((training, holdout), tuning.split(labels))
        self.assertFalse(set(training) & set(holdout))
        self.assertEqual(set(training) | set(holdout), set(labels))

    def test_only_training_labels_become_reference_examples(self):
        inputs = [{"full_name": str(i), "description": "A repo"} for i in range(12)]
        labels = {str(i): {"category": "applications", "subcategories": ["personal"],
                           "keywords": []} for i in range(12)}
        training, holdout = tuning.split(labels)
        examples = tuning.examples(inputs, labels, training, {})
        self.assertTrue(set(e["name"] for e in examples) <= set(training))
        self.assertFalse(set(e["name"] for e in examples) & set(holdout))

    def test_target_drops_teacher_labels_and_bounds_description(self):
        repo = {"full_name": "a/repo", "description": "x" * 65000, "readme": "keep this README",
                "existing_labels": {"category": "models"}}
        target = tuning.target(repo)
        self.assertEqual(len(target["description"]), 1200)
        self.assertEqual(target["readme"], repo["readme"])
        self.assertNotIn("existing_labels", target)

    def test_rerun_calls_only_jev_and_excludes_target_example(self):
        tax = base.load_taxonomy()
        answers = {"category": {"type": "choice", "choice": "ai-engineering", "confidence": .9}}
        answers.update({"sub_" + s: {"type": "noul", "noul": .1} for s in tax.subcategory_slugs})
        answers.update({"keyword_" + s: {"type": "noul", "noul": .1} for s in tax.keyword_slugs})
        body = {"answers": answers, "usage": {"input_tokens": 1000, "output_tokens": 100, "cost": .000042}}
        with tempfile.TemporaryDirectory() as directory, \
                patch.dict(base.os.environ, {"OPENROUTER_API_KEY": "test-key"}), \
                patch.object(base, "http", return_value=Mock(json=lambda: body)) as request:
            tuning.rerun({"full_name": "a/repo"}, 0, Path(directory), tax, {},
                         [{"name": "a/repo"}, {"name": "b/example"}])
            method, endpoint, headers, payload = request.call_args.args
            self.assertEqual(method, "POST")
            self.assertEqual(endpoint, base.JEV_URL)
            self.assertEqual(payload["state"]["reference_examples"], [{"name": "b/example"}])
            self.assertEqual(payload["model"], base.JEV_MODEL)

    def test_bounded_variant_keeps_original_role_policy_and_never_sends_examples(self):
        tax = base.load_taxonomy()
        with tempfile.TemporaryDirectory() as directory, \
                patch.dict(base.os.environ, {"OPENROUTER_API_KEY": "test-key"}), \
                patch.object(tuning, "probabilities"), \
                patch.object(base, "http", return_value=Mock(json=lambda: {})) as request:
            tuning.rerun({"full_name": "a/repo", "description": "x" * 65000}, 0,
                         Path(directory), tax, {}, [{"name": "b/example"}], "bounded")
            payload = request.call_args.args[3]
            self.assertEqual(payload["state"]["classification_policy"], base.build_system_prompt(tax))
            self.assertNotIn("reference_examples", payload["state"])
            self.assertNotIn("x" * 1201, payload["state"]["repository"])


if __name__ == "__main__":
    unittest.main()
