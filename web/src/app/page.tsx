import { db } from "@/lib/db";
import type { Row } from "@libsql/client";
import { RepoTable, type RepoRow } from "./RepoTable";
import { ThemeToggle } from "./ThemeToggle";

export const revalidate = 3600;

async function getAllRepos(): Promise<RepoRow[]> {
  const { rows } = await db.execute(`
    SELECT
      r.full_name,
      r.owner,
      r.name,
      r.description,
      r.url,
      r.tags,
      s_now.stars,
      s_now.forks,
      s_now.issues,
      s_now.primary_language,
      (s_now.stars - s_7d.stars)  AS delta_7d,
      (s_now.stars - s_30d.stars) AS delta_30d,
      s_now.contributors,
      r.owner_type,
      s_now.scraped_date,
      r.owner_country
    FROM repos r
    INNER JOIN snapshots s_now
      ON s_now.id = (
        SELECT id FROM snapshots WHERE repo_id = r.id ORDER BY scraped_date DESC LIMIT 1
      )
    LEFT JOIN snapshots s_7d
      ON r.id = s_7d.repo_id
      AND s_7d.scraped_date = date(s_now.scraped_date, '-7 days')
    LEFT JOIN snapshots s_30d
      ON r.id = s_30d.repo_id
      AND s_30d.scraped_date = date(s_now.scraped_date, '-30 days')
    ORDER BY s_now.stars DESC
  `);

  return rows.map((row: Row) => ({
    full_name: row[0] as string,
    owner: row[1] as string,
    name: row[2] as string,
    description: row[3] as string | null,
    url: row[4] as string,
    tags: JSON.parse((row[5] as string) || "[]") as string[],
    stars: Number(row[6]),
    forks: Number(row[7]),
    issues: Number(row[8]),
    primary_language: row[9] as string | null,
    delta_7d: row[10] != null ? Number(row[10]) : null,
    delta_30d: row[11] != null ? Number(row[11]) : null,
    contributors: row[12] != null ? Number(row[12]) : null,
    owner_type: row[13] as string | null,
    scraped_date: row[14] as string,
    owner_country: (row[15] as string | null) || null,
  }));
}

async function getLatestDate(): Promise<string | null> {
  const { rows } = await db.execute("SELECT MAX(scraped_date) FROM snapshots");
  return rows[0]?.[0] as string | null;
}

export default async function Page() {
  const [repos, latestDate] = await Promise.all([getAllRepos(), getLatestDate()]);

  return (
    <main className="max-w-screen-2xl mx-auto px-6 py-8">
      {/* Header */}
      <div className="mb-8 flex items-start justify-between">
        <div>
          <div className="flex items-baseline gap-3 mb-1">
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-gray-100">Discover open-source LLM projects worth building with</h1>
            <span className="text-xs font-medium px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-400">
              Updated daily
            </span>
          </div>
          <p className="text-gray-500 dark:text-gray-400 text-sm max-w-xl">
            Track the best AI agents, RAG tools, local LLM apps, inference engines, eval frameworks, coding agents, and AI devtools — curated for builders, founders, and researchers.
            Browse {repos.length.toLocaleString()} repos tracked daily.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <a
            href="https://github.com/vince-lam/awesome-local-llms"
            target="_blank"
            rel="noopener noreferrer"
            className="p-2 rounded-md text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            aria-label="View on GitHub"
          >
            <svg viewBox="0 0 24 24" className="w-5 h-5" fill="currentColor" aria-hidden="true">
              <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" />
            </svg>
          </a>
          <ThemeToggle />
        </div>
      </div>

      {repos.length === 0 ? (
        <div className="text-center py-24 text-gray-400">
          <p className="text-lg mb-2">No data yet</p>
          <p className="text-sm">Run the scraper to populate the database.</p>
        </div>
      ) : (
        <RepoTable repos={repos} latestDate={latestDate} />
      )}
    </main>
  );
}
