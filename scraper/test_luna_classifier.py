import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from scraper import classifier, classify, luna_batch, benchmark_luna


class LunaClassifierTest(unittest.TestCase):
    def setUp(self):
        self.tax = classifier.load_taxonomy()
        self.raw = {"category_slug": "ai-engineering", "subcategory_slugs": ["agent-sdk", "coding"],
                    "keyword_slugs": [], "confidence": .9, "reason": "An agent toolkit."}

    def response(self, finish="tool_calls", raw=None):
        return {"choices": [{"finish_reason": finish, "message": {"tool_calls": [
            {"function": {"name": "classify_repo", "arguments": json.dumps(self.raw if raw is None else raw)}}]}}]}

    def request(self):
        return classify._build_request("owner/repo", classifier.build_tool(self.tax),
                                       classifier.build_system_prompt(self.tax),
                                       {"full_name": "owner/repo", "readme": "README context"})

    def test_request_preserves_context_schema_and_disables_reasoning(self):
        request = self.request()
        self.assertEqual(request["url"], "/v1/chat/completions")
        body = request["body"]
        self.assertEqual(body["model"], "gpt-6-luna")
        self.assertEqual(body["reasoning_effort"], "none")
        self.assertIn("README context", body["messages"][1]["content"])
        function = body["tools"][0]["function"]
        self.assertTrue(function["strict"])
        self.assertIn("reason", function["parameters"]["required"])
        self.assertFalse(body["parallel_tool_calls"])

    def test_success_keeps_cross_category_subs_and_reason(self):
        result = classifier.normalise_result(classifier.parse_luna_message(self.response()), self.tax)
        self.assertEqual(result["subcategories"], ["agent-sdk", "coding"])
        self.assertEqual(result["reason"], "An agent toolkit.")

    def test_truncated_refused_or_malformed_response_is_rejected(self):
        cases = [self.response("length"), self.response(raw=[]), self.response(raw={}),
                 self.response(raw={**self.raw, "confidence": True}),
                 self.response(raw={**self.raw, "confidence": float("nan")}),
                 self.response(raw={**self.raw, "subcategory_slugs": "coding"}),
                 self.response(raw={**self.raw, "reason": ""})]
        refused = self.response()
        refused["choices"][0]["message"]["refusal"] = "Refused"
        cases.append(refused)
        malformed = self.response()
        malformed["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"] = "{"
        cases.append(malformed)
        for body in cases:
            with self.subTest(body=body):
                self.assertIsNone(classifier.parse_luna_message(body))

    def test_batch_cache_and_reasoning_cost(self):
        self.assertAlmostEqual(benchmark_luna.cost({"prompt_tokens": 1000, "completion_tokens": 100}), .000075)
        self.assertAlmostEqual(benchmark_luna.cost({"prompt_tokens": 1000, "completion_tokens": 100,
                                                  "prompt_tokens_details": {"cached_tokens": 400, "cache_write_tokens": 200}}), .0000595)

    def test_resume_does_not_submit_and_writes_correct_repo(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            luna_batch.save(path, {"id": "saved", "requests": [self.request()]})
            rows = [{"custom_id": "owner/repo", "response": {"status_code": 200, "body": self.response()}}]
            db, api = Mock(), Mock()
            with patch.object(luna_batch, "collect", return_value=rows), patch.object(luna_batch, "submit") as submit:
                done = classify._run_chunk([], 1, 1, None, None, self.tax, db, api, path)
            submit.assert_not_called()
            self.assertEqual(done, 1)
            self.assertEqual(db.execute.call_args.args[1][-1], "owner/repo")
            self.assertEqual(db.execute.call_args.args[1][5], "accepted")
            self.assertIn("status = 'new'", db.execute.call_args.args[0])
            self.assertFalse(path.exists())

    def test_pending_batch_keeps_state_and_does_not_write(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            luna_batch.save(path, {"id": "saved", "requests": [self.request()]})
            db = Mock()
            with patch.object(luna_batch, "collect", return_value=None):
                self.assertIsNone(classify._run_chunk([], 1, 1, None, None, self.tax, db, Mock(), path))
            db.execute.assert_not_called()
            self.assertTrue(path.exists())

    def test_invalid_and_unknown_results_never_write(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            luna_batch.save(path, {"id": "saved", "requests": [self.request()]})
            rows = [{"custom_id": "other/repo", "response": {"status_code": 200, "body": self.response()}},
                    {"custom_id": "owner/repo", "response": {"status_code": 200, "body": self.response("length")}},
                    {"custom_id": "owner/repo", "error": {"code": "batch_expired"}}]
            db = Mock()
            with patch.object(luna_batch, "collect", return_value=rows):
                self.assertEqual(classify._run_chunk([], 1, 1, None, None, self.tax, db, Mock(), path), 0)
            db.execute.assert_not_called()

    def test_ambiguous_submission_is_not_retried(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            api = Mock()
            api.files.create.return_value = SimpleNamespace(id="file-saved")
            api.batches.create.side_effect = TimeoutError()
            with self.assertRaises(TimeoutError):
                luna_batch.submit(api, [self.request()], path)
            with self.assertRaisesRegex(RuntimeError, "Ambiguous"):
                luna_batch.submit(api, [self.request()], path)
            self.assertEqual(api.batches.create.call_count, 1)

    def test_definite_rejection_clears_guard(self):
        from openai import AuthenticationError
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            api = Mock()
            api.files.create.return_value = SimpleNamespace(id="file-saved")
            response = SimpleNamespace(status_code=401, headers={}, request=Mock())
            api.batches.create.side_effect = AuthenticationError("Rejected", response=response, body=None)
            with self.assertRaises(AuthenticationError):
                luna_batch.submit(api, [self.request()], path)
            self.assertFalse(path.exists())

    def test_failed_validation_retains_state_and_raises(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            api = Mock()
            batch = Mock(status="failed", id="failed-batch")
            batch.model_dump.return_value = {"status": "failed"}
            api.batches.retrieve.return_value = batch
            with self.assertRaisesRegex(RuntimeError, "failed validation"):
                luna_batch.collect(api, {"id": "failed-batch"}, path)
            self.assertTrue(path.exists())
            api.files.content.assert_not_called()

    def test_expired_batch_collects_partial_success_and_error_files(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "batch.json"
            state = {"id": "saved"}
            api = Mock()
            batch = Mock(status="expired", output_file_id="out", error_file_id="err")
            batch.model_dump.return_value = {"status": "expired"}
            api.batches.retrieve.return_value = batch
            api.files.content.side_effect = [SimpleNamespace(text='{"custom_id":"success"}\n'),
                                             SimpleNamespace(text='{"custom_id":"expired"}\n')]
            rows = luna_batch.collect(api, state, path)
            self.assertEqual([r["custom_id"] for r in rows], ["success", "expired"])


if __name__ == "__main__":
    unittest.main()
