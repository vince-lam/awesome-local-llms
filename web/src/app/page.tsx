import { db } from "@/lib/db";
import type { Row } from "@libsql/client";

// Cache for 1 hour — data is refreshed daily by the scraper
export const revalidate = 3600;

type Period = "7d" | "30d" | "1y";

interface RepoRow {
  full_name: string;
  description: string | null;
  url: string;
  tags: string[];
  stars: number;
  forks: number;
  issues: number;
  primary_language: string | null;
  star_delta: number | null;
  latest_date: string | null;
}

async function getTrending(period: Period): Promise<RepoRow[]> {
  const days = period === "7d" ? 7 : period === "30d" ? 30 : 365;

  const { rows } = await db.execute({
    sql: `
      SELECT
        r.full_name,
        r.description,
        r.url,
        r.tags,
        s_now.stars,
        s_now.forks,
        s_now.issues,
        s_now.primary_language,
        (s_now.stars - s_prev.stars)  AS star_delta,
        s_now.scraped_date            AS latest_date
      FROM repos r
      INNER JOIN snapshots s_now
        ON r.id = s_now.repo_id
        AND s_now.scraped_date = (SELECT MAX(scraped_date) FROM snapshots)
      LEFT JOIN snapshots s_prev
        ON r.id = s_prev.repo_id
        AND s_prev.scraped_date = date(
          (SELECT MAX(scraped_date) FROM snapshots),
          '-' || ? || ' days'
        )
      ORDER BY star_delta DESC NULLS LAST, s_now.stars DESC
      LIMIT 500
    `,
    args: [days],
  });

  return rows.map((row: Row) => ({
    full_name: row[0] as string,
    description: row[1] as string | null,
    url: row[2] as string,
    tags: JSON.parse((row[3] as string) || "[]") as string[],
    stars: Number(row[4]),
    forks: Number(row[5]),
    issues: Number(row[6]),
    primary_language: row[7] as string | null,
    star_delta: row[8] != null ? Number(row[8]) : null,
    latest_date: row[9] as string | null,
  }));
}

async function getLatestDate(): Promise<string | null> {
  const { rows } = await db.execute(
    "SELECT MAX(scraped_date) FROM snapshots"
  );
  return rows[0]?.[0] as string | null;
}

function fmt(n: number): string {
  return n.toLocaleString("en-US");
}

function DeltaBadge({ delta }: { delta: number | null }) {
  if (delta == null) return <span className="text-gray-300">—</span>;
  if (delta === 0) return <span className="text-gray-400">+0</span>;
  return (
    <span className={delta > 0 ? "text-emerald-600 font-medium" : "text-red-500"}>
      {delta > 0 ? "+" : ""}
      {fmt(delta)}
    </span>
  );
}

const PERIOD_LABELS: Record<Period, string> = {
  "7d": "7 days",
  "30d": "30 days",
  "1y": "1 year",
};

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ period?: string }>;
}) {
  const { period: raw } = await searchParams;
  const period: Period = (["7d", "30d", "1y"] as Period[]).includes(raw as Period)
    ? (raw as Period)
    : "7d";

  const [repos, latestDate] = await Promise.all([
    getTrending(period),
    getLatestDate(),
  ]);

  return (
    <main className="max-w-screen-xl mx-auto px-4 py-10">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold tracking-tight mb-1">Trending AI Repos</h1>
        <p className="text-gray-500 text-sm">
          {repos.length} repos tracked
          {latestDate && (
            <>
              {" "}· last updated <span className="font-medium">{latestDate}</span>
            </>
          )}
        </p>
      </div>

      {/* Period selector */}
      <div className="flex gap-2 mb-6">
        {(["7d", "30d", "1y"] as Period[]).map((p) => (
          <a
            key={p}
            href={`?period=${p}`}
            className={`px-4 py-1.5 rounded-full text-sm font-medium transition-colors ${
              period === p
                ? "bg-gray-900 text-white"
                : "bg-gray-100 text-gray-600 hover:bg-gray-200"
            }`}
          >
            {PERIOD_LABELS[p]}
          </a>
        ))}
      </div>

      {repos.length === 0 ? (
        <div className="text-center py-24 text-gray-400">
          <p className="text-lg mb-2">No data yet</p>
          <p className="text-sm">Run the scraper to populate the database.</p>
        </div>
      ) : (
        <div className="overflow-x-auto rounded-lg border border-gray-200">
          <table className="w-full text-sm">
            <thead>
              <tr className="bg-gray-50 border-b border-gray-200 text-left text-xs text-gray-500 uppercase tracking-wider">
                <th className="px-4 py-3 w-10">#</th>
                <th className="px-4 py-3">Repository</th>
                <th className="px-4 py-3">Language</th>
                <th className="px-4 py-3 text-right">Stars</th>
                <th className="px-4 py-3 text-right">
                  +Stars ({PERIOD_LABELS[period]})
                </th>
                <th className="px-4 py-3 text-right">Forks</th>
                <th className="px-4 py-3 text-right">Issues</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {repos.map((repo, i) => (
                <tr key={repo.full_name} className="hover:bg-gray-50 transition-colors">
                  <td className="px-4 py-3 text-gray-400 text-xs">{i + 1}</td>
                  <td className="px-4 py-3 max-w-sm">
                    <a
                      href={repo.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="font-semibold text-gray-900 hover:text-blue-600 transition-colors"
                    >
                      {repo.full_name}
                    </a>
                    {repo.description && (
                      <p className="text-gray-400 text-xs mt-0.5 line-clamp-1">
                        {repo.description}
                      </p>
                    )}
                    {repo.tags.length > 0 && (
                      <div className="flex flex-wrap gap-1 mt-1">
                        {repo.tags.slice(0, 3).map((tag) => (
                          <span
                            key={tag}
                            className="text-xs bg-blue-50 text-blue-600 px-1.5 py-0.5 rounded"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </td>
                  <td className="px-4 py-3 text-gray-500 text-xs">
                    {repo.primary_language ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-gray-700">
                    {fmt(repo.stars)}
                  </td>
                  <td className="px-4 py-3 text-right font-mono">
                    <DeltaBadge delta={repo.star_delta} />
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-gray-500">
                    {fmt(repo.forks)}
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-gray-500">
                    {fmt(repo.issues)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </main>
  );
}
