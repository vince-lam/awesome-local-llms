-- Run once to initialise the Turso database:
--   turso db shell <db-name> < db/schema.sql
--
-- Or use the Next.js Drizzle workflow:
--   cd web && npm run db:push

CREATE TABLE IF NOT EXISTS repos (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name   TEXT    NOT NULL UNIQUE,          -- "owner/name"
  owner       TEXT    NOT NULL,
  name        TEXT    NOT NULL,
  description TEXT,
  url         TEXT    NOT NULL,
  category    TEXT,                             -- single category slug (see scraper/data/categories.json)
  tags        TEXT    NOT NULL DEFAULT '[]',    -- JSON array of subcategory slugs (1+)
  keywords    TEXT    NOT NULL DEFAULT '[]',    -- JSON array of keyword slugs (see scraper/data/keywords.json)
  platforms   TEXT    NOT NULL DEFAULT '[]',    -- JSON array
  backends    TEXT    NOT NULL DEFAULT '[]',    -- JSON array
  owner_type    TEXT,                           -- "User" or "Organization" (from GitHub API)
  owner_country    TEXT,                         -- ISO 3166-1 alpha-2 (e.g. "US"), "" = checked/no location, NULL = not yet fetched
  repo_created_at  TEXT,                         -- GitHub repo creation date (YYYY-MM-DD), NULL = not yet fetched
  added_at         TEXT    NOT NULL DEFAULT (date('now')),

  -- Denormalized latest-snapshot cache. Maintained by scraper/update_stats.py
  -- (refresh_denormalized_columns) after each daily snapshot write. The website
  -- reads these instead of recomputing "latest snapshot per repo" with correlated
  -- subqueries over the snapshots table on every request — that pattern scans the
  -- whole snapshots table per page load and is what drives Turso rows-read cost.
  -- Per-repo history (getRepoPage's chart) still reads snapshots directly.
  snapshot_count           INTEGER NOT NULL DEFAULT 0,  -- COUNT(*) of this repo's snapshots
  latest_scraped_date      TEXT,                         -- newest snapshot's date; NULL = no snapshots yet
  latest_stars             INTEGER,
  latest_forks             INTEGER,
  latest_issues            INTEGER,
  latest_watchers          INTEGER,
  latest_contributors      INTEGER,
  latest_days_since_commit INTEGER,
  latest_license           TEXT,
  latest_language          TEXT,                         -- snapshots.primary_language
  delta_1d                 INTEGER,                      -- latest_stars − stars ≤1d before; NULL if no such snapshot
  delta_7d                 INTEGER,                      -- latest_stars − stars ≤7d before
  delta_30d                INTEGER                       -- latest_stars − stars ≤30d before
);

-- The site orders every list by latest stars descending.
CREATE INDEX IF NOT EXISTS idx_repos_latest_stars ON repos(latest_stars DESC);

CREATE TABLE IF NOT EXISTS snapshots (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  repo_id           INTEGER NOT NULL REFERENCES repos(id),
  scraped_date      TEXT    NOT NULL,           -- YYYY-MM-DD
  stars             INTEGER NOT NULL DEFAULT 0,
  forks             INTEGER NOT NULL DEFAULT 0,
  issues            INTEGER NOT NULL DEFAULT 0,
  releases          INTEGER,
  watchers          INTEGER NOT NULL DEFAULT 0,
  days_since_commit INTEGER,
  license           TEXT,
  primary_language  TEXT,
  contributors      INTEGER,
  UNIQUE(repo_id, scraped_date)
);

CREATE INDEX IF NOT EXISTS idx_snap_repo_date ON snapshots(repo_id, scraped_date);
CREATE INDEX IF NOT EXISTS idx_snap_date      ON snapshots(scraped_date);
CREATE INDEX IF NOT EXISTS idx_snap_stars     ON snapshots(stars DESC);

-- Discovery pipeline: repos found by discover.py awaiting triage. A candidate
-- is a repo not yet in the curated repos table. status tracks its lifecycle;
-- rejected rows are kept so discovery never re-surfaces them.
CREATE TABLE IF NOT EXISTS candidates (
  id                    INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name             TEXT    NOT NULL UNIQUE,       -- "owner/name"
  description           TEXT,
  topics                TEXT    NOT NULL DEFAULT '[]', -- JSON array of GitHub topics
  language              TEXT,
  stars                 INTEGER NOT NULL DEFAULT 0,
  archived              INTEGER NOT NULL DEFAULT 0,    -- 0/1
  url                   TEXT,

  -- classification (filled by classify.py)
  suggested_category    TEXT,                          -- category slug
  suggested_subcategory TEXT,                          -- JSON array of subcategory slugs (= repos.tags values)
  suggested_keywords    TEXT,                          -- JSON array of keyword slugs (= repos.keywords values)
  confidence            REAL,                          -- 0.0–1.0
  reason                TEXT,                          -- one-line LLM justification

  -- lifecycle: new | classified | accepted | rejected | duplicate
  status                TEXT    NOT NULL DEFAULT 'new',
  discovered_at         TEXT    NOT NULL DEFAULT (date('now')),
  decided_at            TEXT
);

CREATE INDEX IF NOT EXISTS idx_cand_status ON candidates(status);
CREATE INDEX IF NOT EXISTS idx_cand_stars  ON candidates(stars DESC);

-- Migration for existing databases:
-- ALTER TABLE snapshots ADD COLUMN contributors INTEGER;
-- ALTER TABLE repos ADD COLUMN owner_country TEXT;
-- ALTER TABLE repos ADD COLUMN repo_created_at TEXT;
-- 3-tier taxonomy migration:
-- ALTER TABLE repos ADD COLUMN category TEXT;
-- ALTER TABLE repos ADD COLUMN keywords TEXT NOT NULL DEFAULT '[]';
-- ALTER TABLE candidates ADD COLUMN suggested_keywords TEXT;
-- (candidates table is new — CREATE TABLE IF NOT EXISTS above is safe to re-run)
-- Denormalized latest-snapshot cache migration (run once, then update_stats.py keeps it fresh):
-- ALTER TABLE repos ADD COLUMN snapshot_count INTEGER NOT NULL DEFAULT 0;
-- ALTER TABLE repos ADD COLUMN latest_scraped_date TEXT;
-- ALTER TABLE repos ADD COLUMN latest_stars INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_forks INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_issues INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_watchers INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_contributors INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_days_since_commit INTEGER;
-- ALTER TABLE repos ADD COLUMN latest_license TEXT;
-- ALTER TABLE repos ADD COLUMN latest_language TEXT;
-- ALTER TABLE repos ADD COLUMN delta_1d INTEGER;
-- ALTER TABLE repos ADD COLUMN delta_7d INTEGER;
-- ALTER TABLE repos ADD COLUMN delta_30d INTEGER;
-- CREATE INDEX IF NOT EXISTS idx_repos_latest_stars ON repos(latest_stars DESC);
