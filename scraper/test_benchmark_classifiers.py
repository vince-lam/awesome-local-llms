import argparse
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from scraper import benchmark_classifiers as benchmark


class BenchmarkTest(unittest.TestCase):
    def setUp(self):
        self.tax = benchmark.load_taxonomy()

    def body(self):
        answers = {"category": {"type": "choice", "choice": "ai-engineering", "confidence": 0.9}}
        for slug in self.tax.subcategory_slugs:
            answers["sub_" + slug] = {"type": "noul", "noul": 0.01}
        for slug in self.tax.keyword_slugs:
            answers["keyword_" + slug] = {"type": "noul", "noul": 0.01}
        return {"answers": answers, "usage": {"input_tokens": 6000, "output_tokens": 500, "cost": 0.000252}}

    def test_haiku_baseline_remains_pinned_after_production_migration(self):
        repo = {"full_name": "example/repo", "readme": "README content"}
        params = benchmark.haiku_params(repo, self.tax)
        self.assertEqual(params["model"], "claude-haiku-4-5")
        self.assertEqual(params["max_tokens"], 512)
        self.assertEqual(params["tool_choice"], {"type": "tool", "name": "classify_repo"})
        self.assertIn("README content", params["messages"][0]["content"])

    def test_all_taxonomy_decisions_included(self):
        questions = benchmark.jev_questions(self.tax)
        self.assertEqual(len(questions), 1 + len(self.tax.subcategory_slugs) + len(self.tax.keyword_slugs))
        self.assertEqual(set(questions["category"]["criteria"]), set(self.tax.category_slugs))

    def test_cross_category_tags_survive_with_caps(self):
        body = self.body()
        selected = ["agent-sdk", "coding", "fine-tuning", "local-runtime", "agent-skills", "training"]
        for i, slug in enumerate(selected):
            body["answers"]["sub_" + slug]["noul"] = 0.99 - i * 0.01
        for i, slug in enumerate(self.tax.keyword_slugs[:8]):
            body["answers"]["keyword_" + slug]["noul"] = 0.99 - i * 0.01
        result = benchmark.parse_jev(body, self.tax, 0.5)
        self.assertEqual(result["subcategories"], selected[:5])
        self.assertEqual(result["keywords"], self.tax.keyword_slugs[:6])
        self.assertIsNone(result["reason"])

    def test_missing_confidence_is_not_fabricated(self):
        body = self.body()
        del body["answers"]["category"]["confidence"]
        self.assertIsNone(benchmark.parse_jev(body, self.tax, 0.5)["confidence"])

    def test_incomplete_or_unbilled_results_are_rejected(self):
        body = self.body()
        del body["usage"]["cost"]
        with self.assertRaises(KeyError):
            benchmark.parse_jev(body, self.tax, 0.5)
        body = self.body()
        body["answers"]["sub_" + self.tax.subcategory_slugs[0]]["noul"] = float("nan")
        with self.assertRaises(ValueError):
            benchmark.parse_jev(body, self.tax, 0.5)

    def test_cost_uses_batch_rates_not_output_limit(self):
        self.assertAlmostEqual(benchmark.haiku_cost({"input_tokens": 3000, "output_tokens": 150}), 0.001875)
        self.assertAlmostEqual(benchmark.haiku_cost({"input_tokens": 0, "output_tokens": 0,
                                                  "cache_read_input_tokens": 1000,
                                                  "cache_creation_input_tokens": 1000}), 0.000675)

    def test_frozen_inputs_skip_all_database_and_github_access(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            expected = [{"full_name": "example/repo", "readme": "fixed README"}]
            benchmark.save(output / "inputs.json", expected)
            with patch.object(benchmark, "TursoClient") as client, patch.object(benchmark, "make_github_session") as gh:
                self.assertEqual(benchmark.prepare_inputs(None, output, self.tax), expected)
                client.assert_not_called()
                gh.assert_not_called()

    def test_github_401_identifies_selected_token_without_exposing_it(self):
        with tempfile.TemporaryDirectory() as directory:
            response = Mock(status_code=401, ok=False)
            rows = [("example/repo", "Description", "[]", "Python", 100,
                     "ai-engineering", '["agent-sdk"]', "[]")]
            with patch.dict(benchmark.os.environ, {
                "STATS_GH_PAT": "test-secret", "TURSO_DATABASE_URL": "https://example.invalid",
                "TURSO_AUTH_TOKEN": "test-db-secret"}, clear=True), \
                    patch.object(benchmark, "TursoClient") as db, \
                    patch.object(benchmark, "make_github_session") as session:
                db.return_value.query.return_value = rows
                session.return_value.get.return_value = response
                with self.assertRaises(RuntimeError) as error:
                    benchmark.prepare_inputs(argparse.Namespace(seed=42, limit=1), Path(directory), self.tax)
                self.assertIn("GitHub rejected STATS_GH_PAT (HTTP 401)", str(error.exception))
                self.assertNotIn("test-secret", str(error.exception))
                self.assertFalse((Path(directory) / "inputs.json").exists())

    def test_completed_jev_call_is_not_repeated(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            benchmark.save(output / "jev-000.json", {"status": "succeeded"})
            with patch.object(benchmark, "http") as request:
                benchmark.run_jev({}, 0, None, output, self.tax, {})
                request.assert_not_called()

    def test_input_rejection_is_saved_without_a_paid_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            response = Mock(status_code=400, url=benchmark.JEV_URL)
            response.json.return_value = {"error": {"message": "max_tokens_exceeded"}}
            error = benchmark.ProviderHTTPError(response)
            with patch.dict(benchmark.os.environ, {"OPENROUTER_API_KEY": "test-secret"}), \
                    patch.object(benchmark, "http", side_effect=error) as request:
                benchmark.run_jev({"full_name": "example/repo"}, 0,
                                  argparse.Namespace(threshold=0.5), output, self.tax, {})
                result = benchmark.read(output / "jev-000.json")
                self.assertEqual(result["status"], "rejected")
                self.assertEqual(result["http_status"], 400)
                self.assertFalse((output / "jev-000-pending.json").exists())
                request.assert_called_once()
                benchmark.run_jev({}, 0, None, output, self.tax, {})
                request.assert_called_once()

    def test_ambiguous_submission_cannot_silently_double_bill(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            benchmark.save(output / "jev-000-pending.json", {})
            with patch.object(benchmark, "http") as request:
                with self.assertRaisesRegex(RuntimeError, "Ambiguous"):
                    benchmark.run_jev({}, 0, None, output, self.tax, {})
                request.assert_not_called()

    def test_summary_uses_reported_usage_and_measures_label_overlap(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            classification = {"category": "ai-engineering", "subcategories": ["agent-sdk"],
                              "keywords": ["rag"]}
            inputs = [{"full_name": "example/repo", "readme": "README"}]
            benchmark.save(output / "haiku-results.json", [{
                "full_name": "example/repo", "classification": classification,
                "usage": {"input_tokens": 3000, "output_tokens": 150}, "cost": 0.001875}])
            benchmark.save(output / "jev-000.json", {
                "full_name": "example/repo", "classification": classification,
                "raw": self.body(), "seconds": 0.5, "status": "succeeded"})
            benchmark.save(output / "haiku-batch.json", {
                "submitted_at": "2026-10-01T00:00:00+00:00", "ended_at": "2026-10-01T00:02:00Z"})
            benchmark.save(output / "jev-run.json", {
                "started_at": "2026-10-01T00:00:00+00:00", "ended_at": "2026-10-01T00:00:01+00:00"})
            with patch("builtins.print"):
                benchmark.summarise(output, inputs)
            summary = benchmark.read(output / "summary.json")
            self.assertAlmostEqual(summary["haiku"]["cost_per_1000_submitted"], 1.875)
            self.assertAlmostEqual(summary["jev"]["cost_per_1000_submitted"], 0.252)
            self.assertEqual(summary["category_agreement"], 1)
            self.assertEqual(summary["subcategories_mean_jaccard"], 1)
            self.assertEqual(summary["haiku"]["batch_completion_seconds"], 120)
            self.assertEqual(summary["jev"]["wall_completion_seconds"], 1)
            self.assertEqual(benchmark.read(output / "disagreements.json"), [])


if __name__ == "__main__":
    unittest.main()
