"""
Minimal Turso (libSQL) HTTP client, shared by scrape.py, discover.py, and
classify.py.

Talks to the Turso /v2/pipeline HTTP API directly (no libsql driver dependency).

Environment variables used by callers:
  TURSO_DATABASE_URL   — libsql://... URL from the Turso dashboard
  TURSO_AUTH_TOKEN     — Turso auth token
"""

from typing import Optional

import requests


def _arg(v) -> dict:
    if v is None:
        return {"type": "null"}
    if isinstance(v, bool):
        return {"type": "integer", "value": str(int(v))}
    if isinstance(v, int):
        return {"type": "integer", "value": str(v)}
    if isinstance(v, float):
        # Turso expects f64 as a JSON number, not a string (unlike integers).
        return {"type": "float", "value": v}
    return {"type": "text", "value": str(v)}


class TursoClient:
    def __init__(self, url: str, token: str) -> None:
        # Accept libsql:// or https://
        self.base_url = url.replace("libsql://", "https://").rstrip("/")
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _pipeline(self, stmts: list[dict]) -> list[dict]:
        payload = {
            "requests": [{"type": "execute", "stmt": s} for s in stmts]
            + [{"type": "close"}]
        }
        r = requests.post(
            f"{self.base_url}/v2/pipeline",
            json=payload,
            headers=self._headers,
            timeout=30,
        )
        r.raise_for_status()
        results = r.json().get("results", [])
        for res in results:
            if res.get("type") == "error":
                raise RuntimeError(f"Turso: {res['error']['message']}")
        return results

    def execute(self, sql: str, args: Optional[list] = None) -> dict:
        stmt: dict = {"sql": sql}
        if args:
            stmt["args"] = [_arg(a) for a in args]
        return self._pipeline([stmt])[0]

    def executemany(self, statements: list[tuple[str, list]]) -> list[dict]:
        stmts = []
        for sql, args in statements:
            stmt: dict = {"sql": sql}
            if args:
                stmt["args"] = [_arg(a) for a in args]
            stmts.append(stmt)
        return self._pipeline(stmts)

    def query(self, sql: str, args: Optional[list] = None) -> list[list]:
        """Run a SELECT and return rows as plain Python lists."""
        res = self.execute(sql, args)
        raw_rows = res.get("response", {}).get("result", {}).get("rows", [])
        def _val(v: dict):
            if v["type"] == "null":
                return None
            if v["type"] == "integer":
                return int(v["value"])
            if v["type"] == "float":
                return float(v["value"])
            return v["value"]
        return [[_val(cell) for cell in row] for row in raw_rows]
