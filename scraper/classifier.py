"""
Shared LLM classification core for the 3-tier taxonomy.

classify.py (new discovered candidates) and triage_batch.py import from here so
the taxonomy, the constrained tool, and the validation logic live in exactly one
place.

A classification is: one category, one-or-more subcategories (each belonging to
that category), and zero-or-more cross-cutting keywords — all drawn from the
fixed vocabularies in data/categories.json and data/keywords.json. The model is
constrained via enum'd tool inputs so it cannot invent slugs.
"""

import json
import os
import time

import requests

MODEL = "claude-haiku-4-5"   # cheap + fast; bump to claude-sonnet-4-6 if quality is weak

README_MAX_CHARS = 4000      # ~1k tokens of README context per repo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")
KEYWORDS_FILE = os.path.join(DATA_DIR, "keywords.json")

MAX_SUBCATEGORIES = 5
MAX_KEYWORDS = 6


class Taxonomy:
    """Loaded taxonomy plus the lookups needed to build prompts and validate."""

    def __init__(self, categories: list[dict], keywords: list[dict]):
        self.categories = categories
        self.keywords = keywords

        self.subcats: list[dict] = []          # {category, category_slug, name, slug}
        self.sub_to_cat: dict[str, str] = {}   # subcategory slug → category slug
        self.subs_by_cat: dict[str, list[str]] = {}  # category slug → [sub slug]
        for cat in categories:
            self.subs_by_cat[cat["slug"]] = []
            for sub in cat["subcategories"]:
                self.subcats.append({
                    "category": cat["category"],
                    "category_slug": cat["slug"],
                    "name": sub["name"],
                    "slug": sub["slug"],
                })
                self.sub_to_cat[sub["slug"]] = cat["slug"]
                self.subs_by_cat[cat["slug"]].append(sub["slug"])

        self.category_slugs = [c["slug"] for c in categories]
        self.subcategory_slugs = [s["slug"] for s in self.subcats]
        self.keyword_slugs = [k["slug"] for k in keywords]
        self._cat_set = set(self.category_slugs)
        self._sub_set = set(self.subcategory_slugs)
        self._keyword_set = set(self.keyword_slugs)


def load_taxonomy() -> Taxonomy:
    with open(CATEGORIES_FILE, encoding="utf-8") as f:
        categories = json.load(f)
    with open(KEYWORDS_FILE, encoding="utf-8") as f:
        keywords = json.load(f)
    return Taxonomy(categories, keywords)


def build_system_prompt(tax: Taxonomy) -> str:
    lines = [
        "You classify open-source LLM/AI GitHub repositories into a fixed taxonomy.",
        "The taxonomy is three tiers:",
        "  1. category      — one broad bucket (what kind of thing the repo is).",
        "  2. subcategories — one or more specific roles (up to 5). Assign every",
        "     subcategory that genuinely applies; they MAY span categories when a",
        "     repo wears more than one hat (e.g. a model that ships a training",
        "     toolkit). Pick the single best-fitting category above as primary.",
        "  3. keywords      — cross-cutting facets (techniques, integrations,",
        "     modalities, domains) that need not match the category. Pick only",
        "     keywords the repo is clearly about; an empty list is fine.",
        "Use the repo's name, description, topics, language and README (when",
        "provided). If genuinely unsure, still pick the closest fit but lower",
        "your confidence.",
        "",
        "Categories and their subcategories:",
    ]
    for cat in tax.categories:
        lines.append(f"{cat['category']} (slug: {cat['slug']}):")
        for sub in cat["subcategories"]:
            lines.append(f"  - {sub['name']} (slug: {sub['slug']})")
    lines.append("")
    lines.append("Available keywords (slugs): " + ", ".join(tax.keyword_slugs))
    return "\n".join(lines)


def build_tool(tax: Taxonomy) -> dict:
    return {
        "name": "classify_repo",
        "description": "Record the category, subcategories and keywords for this repository.",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "category_slug": {
                    "type": "string",
                    "enum": tax.category_slugs,
                    "description": "Slug of the single best-fitting category.",
                },
                "subcategory_slugs": {
                    "type": "array",
                    "items": {"type": "string", "enum": tax.subcategory_slugs},
                    "description": (
                        "One to five subcategory slugs — every role that genuinely "
                        "applies. May span categories; the primary category is chosen "
                        "separately."
                    ),
                },
                "keyword_slugs": {
                    "type": "array",
                    "items": {"type": "string", "enum": tax.keyword_slugs},
                    "description": "Zero to six cross-cutting keyword slugs. Empty if none clearly apply.",
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence in this classification, 0.0 to 1.0.",
                },
                "reason": {
                    "type": "string",
                    "description": "One-line justification (<= 120 characters).",
                },
            },
            "required": [
                "category_slug", "subcategory_slugs", "keyword_slugs",
                "confidence", "reason",
            ],
            "additionalProperties": False,
        },
    }


def make_github_session(token: str | None) -> requests.Session:
    s = requests.Session()
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    s.headers.update(headers)
    return s


def github_token() -> str | None:
    return (
        os.getenv("STATS_GH_PAT")
        or os.getenv("GITHUB_TOKEN")
        or os.getenv("GITHUB_API_TOKEN")
    )


def fetch_readme(session: requests.Session, full_name: str,
                 max_chars: int = README_MAX_CHARS) -> str | None:
    """Best-effort raw README text, truncated. Returns None on any failure."""
    url = f"https://api.github.com/repos/{full_name}/readme"
    headers = {"Accept": "application/vnd.github.raw+json"}
    try:
        resp = session.get(url, headers=headers, timeout=30)
    except requests.RequestException:
        return None

    if resp.status_code in (403, 429):
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset - time.time()) + 5
        print(f"    Rate limited (readme) — sleeping {wait:.0f}s")
        time.sleep(wait)
        try:
            resp = session.get(url, headers=headers, timeout=30)
        except requests.RequestException:
            return None

    if not resp.ok:
        return None
    text = resp.text or ""
    return text[:max_chars].strip() or None


def format_repo_prompt(repo: dict) -> str:
    """Build the user message from a repo/candidate dict."""
    topics = repo.get("topics") or []
    topics_str = ", ".join(topics) if topics else "(none)"
    stars = repo.get("stars") or 0
    lines = [
        f"Repository: {repo['full_name']}",
        f"Description: {repo.get('description') or '(none)'}",
        f"Primary language: {repo.get('language') or '(unknown)'}",
        f"GitHub topics: {topics_str}",
        f"Stars: {stars:,}",
    ]
    readme = repo.get("readme")
    if readme:
        lines.append("")
        lines.append("README (truncated):")
        lines.append(readme)
    return "\n".join(lines)


def classify_one(client, tool: dict, system: str, repo: dict) -> dict | None:
    """Call the model; return the raw tool input, or None if none returned."""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=system,
        tools=[tool],
        tool_choice={"type": "tool", "name": "classify_repo"},
        messages=[{"role": "user", "content": format_repo_prompt(repo)}],
    )
    for block in resp.content:
        if block.type == "tool_use" and block.name == "classify_repo":
            return block.input
    return None


def normalise_result(result: dict, tax: Taxonomy) -> dict:
    """
    Reconcile the model output into a consistent classification:

      - keep the chosen primary category (one only); if it isn't a valid
        category slug, derive it from the first valid subcategory's parent;
      - keep every valid subcategory, which MAY span categories (a repo can
        wear more than one hat) — capped at MAX_SUBCATEGORIES;
      - drop any keyword not in the vocabulary — capped at MAX_KEYWORDS.

    Returns {category, subcategories, keywords, confidence, reason}.
    """
    category = result.get("category_slug")
    subs = [s for s in dict.fromkeys(result.get("subcategory_slugs") or [])
            if s in tax._sub_set][:MAX_SUBCATEGORIES]

    # Primary category: trust the explicit choice if valid, else fall back to
    # the parent of the first subcategory so we never lose the label.
    if category not in tax._cat_set:
        category = tax.sub_to_cat.get(subs[0]) if subs else None

    keywords = [k for k in dict.fromkeys(result.get("keyword_slugs") or [])
                if k in tax._keyword_set][:MAX_KEYWORDS]

    return {
        "category": category,
        "subcategories": subs,
        "keywords": keywords,
        "confidence": float(result.get("confidence") or 0.0),
        "reason": result.get("reason") or "",
    }
