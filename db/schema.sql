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
  tags        TEXT    NOT NULL DEFAULT '[]',    -- JSON array of tag slugs
  platforms   TEXT    NOT NULL DEFAULT '[]',    -- JSON array
  backends    TEXT    NOT NULL DEFAULT '[]',    -- JSON array
  owner_type    TEXT,                           -- "User" or "Organization" (from GitHub API)
  owner_country    TEXT,                         -- ISO 3166-1 alpha-2 (e.g. "US"), "" = checked/no location, NULL = not yet fetched
  repo_created_at  TEXT,                         -- GitHub repo creation date (YYYY-MM-DD), NULL = not yet fetched
  added_at         TEXT    NOT NULL DEFAULT (date('now'))
);

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
  suggested_subcategory TEXT,                          -- subcategory slug = a repos.tags value
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
-- (candidates table is new — CREATE TABLE IF NOT EXISTS above is safe to re-run)
