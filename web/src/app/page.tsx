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
      r.owner_type
    FROM repos r
    INNER JOIN snapshots s_now
      ON r.id = s_now.repo_id
      AND s_now.scraped_date = (SELECT MAX(scraped_date) FROM snapshots)
    LEFT JOIN snapshots s_7d
      ON r.id = s_7d.repo_id
      AND s_7d.scraped_date = date((SELECT MAX(scraped_date) FROM snapshots), '-7 days')
    LEFT JOIN snapshots s_30d
      ON r.id = s_30d.repo_id
      AND s_30d.scraped_date = date((SELECT MAX(scraped_date) FROM snapshots), '-30 days')
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
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-gray-100">llm repos</h1>
            <span className="text-xs font-medium px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-400">
              Updated daily
            </span>
          </div>
          <p className="text-gray-400 dark:text-gray-500 text-sm">
            {repos.length.toLocaleString()} curated AI &amp; LLM GitHub repositories, tracked daily
          </p>
        </div>
        <ThemeToggle />
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
