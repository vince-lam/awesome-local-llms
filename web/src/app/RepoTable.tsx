"use client";

import { useState, useMemo } from "react";
import Image from "next/image";

export interface RepoRow {
  full_name: string;
  owner: string;
  name: string;
  description: string | null;
  url: string;
  tags: string[];
  stars: number;
  forks: number;
  issues: number;
  primary_language: string | null;
  delta_7d: number | null;
  delta_30d: number | null;
  contributors: number | null;
  owner_type: string | null;
  scraped_date: string;
  owner_country: string | null;
}

// subcategory slug → { category, categorySlug, subcategory }
const CATEGORIES = [
  { category: "Inference & Runtime", slug: "inference-runtime", subcategories: [
    { name: "Local Runtime", slug: "local-runtime" },
    { name: "Fine-Tuning", slug: "fine-tuning" },
    { name: "Production Serving", slug: "production-serving" },
    { name: "Distributed Inference", slug: "distributed-inference" },
    { name: "Web / Edge Runtime", slug: "web-edge-runtime" },
    { name: "Bindings & SDKs", slug: "bindings-sdks" },
  ]},
  { category: "Chat Interface", slug: "chat-interface", subcategories: [
    { name: "Desktop App", slug: "desktop-app" },
    { name: "Web App", slug: "web-app" },
    { name: "Mobile App", slug: "mobile-app" },
    { name: "CLI / Terminal", slug: "cli-terminal" },
    { name: "Browser Extension", slug: "browser-extension" },
  ]},
  { category: "Agentic Framework", slug: "agentic-framework", subcategories: [
    { name: "Orchestration", slug: "orchestration" },
    { name: "Multi-Agent System", slug: "multi-agent-system" },
    { name: "Workflow / Low-code", slug: "workflow-low-code" },
    { name: "Memory & State", slug: "memory-state" },
    { name: "MCP Server / Tool", slug: "mcp-server" },
    { name: "Voice Agent", slug: "voice-agent" },
    { name: "Computer Use", slug: "computer-use" },
  ]},
  { category: "Coding Assistant", slug: "coding-assistant", subcategories: [
    { name: "IDE Plugin", slug: "ide-plugin" },
    { name: "Code Review", slug: "code-review" },
    { name: "CLI Tool", slug: "cli-tool" },
    { name: "Pair Programmer", slug: "pair-programmer" },
  ]},
  { category: "Research & Knowledge", slug: "research-knowledge", subcategories: [
    { name: "RAG / Search", slug: "rag-search" },
    { name: "Document QA", slug: "document-qa" },
    { name: "Knowledge Graph", slug: "knowledge-graph" },
  ]},
  { category: "Data & Analytics", slug: "data-analytics", subcategories: [
    { name: "Data Pipeline", slug: "data-pipeline" },
    { name: "Analytics / BI", slug: "analytics-bi" },
  ]},
  { category: "Web & Browser Agent", slug: "web-browser-agent", subcategories: [
    { name: "Web Scraping", slug: "web-scraping" },
    { name: "Browser Automation", slug: "browser-automation" },
  ]},
  { category: "General Autonomous Agent", slug: "general-autonomous-agent", subcategories: [
    { name: "Task Automation", slug: "task-automation" },
    { name: "Personal Assistant", slug: "personal-assistant" },
  ]},
  { category: "Gaming & Simulation", slug: "gaming-simulation", subcategories: [
    { name: "Game AI", slug: "game-ai" },
    { name: "Simulation", slug: "simulation" },
  ]},
  { category: "LLM Ops & Evaluation", slug: "llm-ops-evaluation", subcategories: [
    { name: "Evaluation / Benchmarks", slug: "evaluation-benchmarks" },
    { name: "Monitoring & Observability", slug: "monitoring-observability" },
  ]},
] as const;

type SubcategoryInfo = { category: string; categorySlug: string; name: string; slug: string };

const SUBCATEGORY_MAP: Record<string, SubcategoryInfo> = {};
for (const cat of CATEGORIES) {
  for (const sub of cat.subcategories) {
    SUBCATEGORY_MAP[sub.slug] = {
      category: cat.category,
      categorySlug: cat.slug,
      name: sub.name,
      slug: sub.slug,
    };
  }
}

const CATEGORY_COLORS: Record<string, { bg: string; text: string }> = {
  "inference-runtime":         { bg: "bg-purple-100 dark:bg-purple-900/40", text: "text-purple-700 dark:text-purple-300" },
  "chat-interface":            { bg: "bg-blue-100 dark:bg-blue-900/40",     text: "text-blue-700 dark:text-blue-300" },
  "agentic-framework":         { bg: "bg-orange-100 dark:bg-orange-900/40", text: "text-orange-700 dark:text-orange-300" },
  "coding-assistant":          { bg: "bg-green-100 dark:bg-green-900/40",   text: "text-green-700 dark:text-green-300" },
  "research-knowledge":        { bg: "bg-teal-100 dark:bg-teal-900/40",     text: "text-teal-700 dark:text-teal-300" },
  "data-analytics":            { bg: "bg-yellow-100 dark:bg-yellow-900/40", text: "text-yellow-700 dark:text-yellow-300" },
  "web-browser-agent":         { bg: "bg-cyan-100 dark:bg-cyan-900/40",     text: "text-cyan-700 dark:text-cyan-300" },
  "general-autonomous-agent":  { bg: "bg-red-100 dark:bg-red-900/40",       text: "text-red-700 dark:text-red-300" },
  "gaming-simulation":         { bg: "bg-indigo-100 dark:bg-indigo-900/40", text: "text-indigo-700 dark:text-indigo-300" },
  "llm-ops-evaluation":        { bg: "bg-pink-100 dark:bg-pink-900/40",     text: "text-pink-700 dark:text-pink-300" },
};

type SortKey = "stars" | "delta_7d" | "delta_30d" | "forks" | "issues" | "contributors";
type SortDir = "desc" | "asc";

function fmt(n: number): string {
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  if (n >= 1_000) return (n / 1_000).toFixed(1).replace(/\.0$/, "") + "k";
  return n.toLocaleString("en-US");
}

function DeltaBadge({ delta }: { delta: number | null }) {
  if (delta == null) return <span className="text-gray-300 dark:text-gray-600">—</span>;
  if (delta === 0) return <span className="text-gray-400 dark:text-gray-500">+0</span>;
  return (
    <span className={delta > 0 ? "text-emerald-600 dark:text-emerald-400 font-medium" : "text-red-500 dark:text-red-400"}>
      {delta > 0 ? "+" : ""}
      {fmt(delta)}
    </span>
  );
}

function SortIcon({ active, dir }: { active: boolean; dir: SortDir }) {
  if (!active) return <span className="ml-1 text-gray-300 dark:text-gray-600 text-xs">↕</span>;
  return <span className="ml-1 text-gray-700 dark:text-gray-300 text-xs">{dir === "desc" ? "↓" : "↑"}</span>;
}

function countryFlag(code: string): string {
  return [...code.toUpperCase()].map(c =>
    String.fromCodePoint(c.charCodeAt(0) + 0x1F1A5)
  ).join("");
}

function wrapAtSpaces(text: string) {
  return text.split(" ").join(" ​");
}

function TagPill({ tag }: { tag: string }) {
  const info = SUBCATEGORY_MAP[tag];
  if (!info) return null;
  const colors = CATEGORY_COLORS[info.categorySlug] ?? { bg: "bg-gray-100", text: "text-gray-600" };
  return (
    <span
      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-xs font-medium ${colors.bg} ${colors.text}`}
      style={{ overflowWrap: "anywhere" }}
    >
      {wrapAtSpaces(info.name)}
    </span>
  );
}

function CategoryPill({ categorySlug, categoryName }: { categorySlug: string; categoryName: string }) {
  const colors = CATEGORY_COLORS[categorySlug] ?? { bg: "bg-gray-100", text: "text-gray-600" };
  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-semibold ${colors.bg} ${colors.text}`}
      style={{ overflowWrap: "anywhere" }}
    >
      {wrapAtSpaces(categoryName)}
    </span>
  );
}

const PAGE_SIZES = [100, 200, 500] as const;
type PageSize = typeof PAGE_SIZES[number];

const COL_KEYS = ["rank","repo","stars","d7","d30","forks","contributors","description","category","subcat","issues","language"] as const;
type ColKey = typeof COL_KEYS[number];

const COL_WIDTHS: Record<ColKey, number> = {
  rank: 32, repo: 140, stars: 84, d7: 64, d30: 64, forks: 70,
  contributors: 82, description: 400, category: 114, subcat: 104, issues: 68, language: 72,
};

const DESCRIPTION_MOBILE_LIMIT = 100;

function DescriptionCell({ text }: { text: string | null }) {
  const [expanded, setExpanded] = useState(false);

  if (!text) {
    return <span className="text-gray-300 dark:text-gray-600 italic">—</span>;
  }

  const needsTruncation = text.length > DESCRIPTION_MOBILE_LIMIT;

  return (
    <span className="text-gray-500 dark:text-gray-400 leading-relaxed break-words">
      <span className="md:hidden">
        {needsTruncation && !expanded ? `${text.slice(0, DESCRIPTION_MOBILE_LIMIT)}…` : text}
        {needsTruncation && (
          <button
            onClick={(e) => { e.stopPropagation(); setExpanded((x) => !x); }}
            className="ml-1 text-blue-500 hover:text-blue-700 dark:hover:text-blue-300 text-xs underline"
          >
            {expanded ? "less" : "more"}
          </button>
        )}
      </span>
      <span className="hidden md:inline">{text}</span>
    </span>
  );
}

export function RepoTable({ repos, latestDate }: { repos: RepoRow[]; latestDate: string | null }) {
  const [search, setSearch] = useState("");
  const [activeCats, setActiveCats] = useState<Set<string>>(new Set());
  const [activeSubs, setActiveSubs] = useState<Set<string>>(new Set());
  const [sortKey, setSortKey] = useState<SortKey>("stars");
  const [sortDir, setSortDir] = useState<SortDir>("desc");
  const [pageSize, setPageSize] = useState<PageSize>(100);
  const [page, setPage] = useState(0);
  // Collect all categories that actually appear in the data
  const presentCategories = useMemo(() => {
    const catSlugs = new Set<string>();
    for (const repo of repos) {
      for (const tag of repo.tags) {
        const info = SUBCATEGORY_MAP[tag];
        if (info) catSlugs.add(info.categorySlug);
      }
    }
    return CATEGORIES.filter((c) => catSlugs.has(c.slug));
  }, [repos]);

  // Subcategories to show based on active category filter
  const presentSubcategories = useMemo(() => {
    const subSlugs = new Set<string>();
    for (const repo of repos) {
      for (const tag of repo.tags) {
        const info = SUBCATEGORY_MAP[tag];
        if (!info) continue;
        if (activeCats.size === 0 || activeCats.has(info.categorySlug)) {
          subSlugs.add(tag);
        }
      }
    }
    const result: SubcategoryInfo[] = [];
    for (const cat of CATEGORIES) {
      for (const sub of cat.subcategories) {
        if (subSlugs.has(sub.slug)) {
          result.push({ category: cat.category, categorySlug: cat.slug, name: sub.name, slug: sub.slug });
        }
      }
    }
    return result;
  }, [repos, activeCats]);

  function toggleCat(slug: string) {
    setActiveCats((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) { next.delete(slug); } else { next.add(slug); }
      return next;
    });
    setActiveSubs(new Set());
    setPage(0);
  }

  function toggleSub(slug: string) {
    setActiveSubs((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) { next.delete(slug); } else { next.add(slug); }
      return next;
    });
    setPage(0);
  }

  function handleSort(key: SortKey) {
    if (sortKey === key) {
      setSortDir((d) => (d === "desc" ? "asc" : "desc"));
    } else {
      setSortKey(key);
      setSortDir("desc");
    }
    setPage(0);
  }

  const filtered = useMemo(() => {
    const q = search.toLowerCase().trim();
    return repos.filter((repo) => {
      if (q && !repo.full_name.toLowerCase().includes(q) && !repo.description?.toLowerCase().includes(q)) {
        return false;
      }
      if (activeCats.size > 0) {
        const repoCats = new Set(repo.tags.map((t) => SUBCATEGORY_MAP[t]?.categorySlug).filter(Boolean));
        if (![...activeCats].some((c) => repoCats.has(c))) return false;
      }
      if (activeSubs.size > 0) {
        if (![...activeSubs].some((s) => repo.tags.includes(s))) return false;
      }
      return true;
    });
  }, [repos, search, activeCats, activeSubs]);

  const sorted = useMemo(() => {
    return [...filtered].sort((a, b) => {
      const av = a[sortKey] ?? -Infinity;
      const bv = b[sortKey] ?? -Infinity;
      return sortDir === "desc" ? (bv as number) - (av as number) : (av as number) - (bv as number);
    });
  }, [filtered, sortKey, sortDir]);

  const totalPages = Math.ceil(sorted.length / pageSize);
  const paginated = sorted.slice(page * pageSize, (page + 1) * pageSize);

  const clearFilters = activeCats.size > 0 || activeSubs.size > 0 || search;

  return (
    <div>
      {/* Search + stats bar */}
      <div className="flex flex-col sm:flex-row gap-3 mb-5 items-start sm:items-center">
        <div className="relative flex-1 max-w-md">
          <svg className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            type="text"
            placeholder="Search repos or descriptions…"
            value={search}
            onChange={(e) => { setSearch(e.target.value); setPage(0); }}
            className="w-full pl-9 pr-4 py-2 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <p className="text-sm text-gray-400 dark:text-gray-500 whitespace-nowrap">
          {sorted.length.toLocaleString()} of {repos.length.toLocaleString()} repos
          {latestDate && (
            <> · updated <span className="font-medium text-gray-500 dark:text-gray-400">{latestDate}</span></>
          )}
        </p>
        {clearFilters && (
          <button
            onClick={() => { setSearch(""); setActiveCats(new Set()); setActiveSubs(new Set()); setPage(0); }}
            className="text-xs text-blue-500 hover:text-blue-700 underline whitespace-nowrap"
          >
            Clear filters
          </button>
        )}
        <div className="flex items-center gap-1 ml-auto">
          <span className="text-xs text-gray-400 dark:text-gray-500 whitespace-nowrap">Show</span>
          {PAGE_SIZES.map((s) => (
            <button
              key={s}
              onClick={() => { setPageSize(s); setPage(0); }}
              className={`px-2 py-0.5 rounded text-xs border transition-colors ${
                pageSize === s
                  ? "bg-gray-800 dark:bg-gray-200 text-white dark:text-gray-900 border-gray-800 dark:border-gray-200"
                  : "bg-white dark:bg-gray-900 text-gray-500 dark:text-gray-400 border-gray-200 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500"
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      {/* Category filter chips */}
      <div className="mb-3">
        <div className="flex flex-wrap gap-1.5">
          {presentCategories.map((cat) => {
            const colors = CATEGORY_COLORS[cat.slug] ?? { bg: "bg-gray-100 dark:bg-gray-800", text: "text-gray-600 dark:text-gray-300" };
            const active = activeCats.has(cat.slug);
            return (
              <button
                key={cat.slug}
                onClick={() => toggleCat(cat.slug)}
                className={`px-3 py-1 rounded-full text-xs font-semibold border transition-all ${
                  active
                    ? `${colors.bg} ${colors.text} border-transparent ring-2 ring-offset-1 dark:ring-offset-gray-950 ring-current`
                    : "bg-white dark:bg-gray-900 text-gray-500 dark:text-gray-400 border-gray-200 dark:border-gray-700 hover:border-gray-400 dark:hover:border-gray-500"
                }`}
              >
                {cat.category}
              </button>
            );
          })}
        </div>
      </div>

      {/* Subcategory filter chips */}
      {presentSubcategories.length > 0 && (
        <div className="mb-5">
          <div className="flex flex-wrap gap-1">
            {presentSubcategories.map((sub) => {
              const active = activeSubs.has(sub.slug);
              return (
                <button
                  key={sub.slug}
                  onClick={() => toggleSub(sub.slug)}
                  className={`px-2.5 py-0.5 rounded text-xs border transition-all ${
                    active
                      ? "bg-gray-800 dark:bg-gray-200 text-white dark:text-gray-900 border-gray-800 dark:border-gray-200"
                      : "bg-gray-50 dark:bg-gray-800 text-gray-500 dark:text-gray-400 border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-700 dark:hover:text-gray-200"
                  }`}
                >
                  {sub.name}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Table */}
      {sorted.length === 0 ? (
        <div className="text-center py-20 text-gray-400">
          <p className="text-lg mb-1">No repos match your filters</p>
          <p className="text-sm">Try broadening your search or clearing filters.</p>
        </div>
      ) : (
        <div className="overflow-x-auto rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm">
          <table className="text-xs w-full min-w-[1300px]" style={{ tableLayout: "fixed" }}>
            <colgroup>
              {COL_KEYS.map(k => <col key={k} style={k === "description" ? { minWidth: COL_WIDTHS[k] } : { width: COL_WIDTHS[k] }} />)}
            </colgroup>
            <thead>
              <tr className="bg-gray-50 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 text-left text-[10px] text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {([
                  { key: "rank",         label: "#",           right: false, center: true,  sort: null },
                  { key: "repo",         label: "Repo",        right: false, center: false, sort: null },
                  { key: "stars",        label: "Stars",       right: true,  center: false, sort: "stars" as SortKey },
                  { key: "d7",           label: "7d",          right: true,  center: false, sort: "delta_7d" as SortKey },
                  { key: "d30",          label: "30d",         right: true,  center: false, sort: "delta_30d" as SortKey },
                  { key: "forks",        label: "Forks",       right: true,  center: false, sort: "forks" as SortKey },
                  { key: "contributors", label: "Contribs",    right: true,  center: false, sort: "contributors" as SortKey },
                  { key: "description",  label: "Description", right: false, center: false, sort: null },
                  { key: "category",     label: "Category",    right: false, center: false, sort: null },
                  { key: "subcat",       label: "Subcat",      right: false, center: false, sort: null },
                  { key: "issues",       label: "Issues",      right: true,  center: false, sort: "issues" as SortKey },
                  { key: "language",     label: "Language",    right: false, center: false, sort: null },
                ] satisfies { key: ColKey; label: string; right: boolean; center: boolean; sort: SortKey | null }[]).map(col => (
                  <th
                    key={col.key}
                    className={`p-0 select-none ${col.sort ? "cursor-pointer" : ""}`}
                    onClick={col.sort ? () => handleSort(col.sort!) : undefined}
                  >
                    <div className={`px-2 py-2 overflow-hidden whitespace-nowrap ${col.center ? "text-center" : col.right ? "text-right" : "text-left"} ${col.sort ? "hover:text-gray-700 dark:hover:text-gray-300" : ""}`}>
                      {col.label}{col.sort && <SortIcon active={sortKey === col.sort} dir={sortDir} />}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 dark:divide-gray-800">
              {paginated.map((repo, i) => {
                const globalIndex = page * pageSize + i;
                const catSlugs = [...new Set(repo.tags.map((t) => SUBCATEGORY_MAP[t]?.categorySlug).filter(Boolean) as string[])];
                const isStale = latestDate != null && repo.scraped_date !== latestDate;
                return (
                  <tr key={repo.full_name} className={`transition-colors group ${repo.owner_type === "Organization" ? "bg-purple-50/40 dark:bg-purple-950/20 hover:bg-purple-100/40 dark:hover:bg-purple-900/20" : "hover:bg-blue-50/30 dark:hover:bg-blue-950/20"}`}>
                    <td className="px-2 py-2 text-gray-400 dark:text-gray-600 text-center overflow-hidden">{globalIndex + 1}</td>
                    <td className="px-2 py-2 overflow-hidden">
                      <div className="flex items-center gap-2">
                        <Image
                          src={`https://github.com/${repo.owner}.png?size=64`}
                          alt={repo.owner}
                          width={28}
                          height={28}
                          className="rounded-full shrink-0"
                          unoptimized
                        />
                        <div className="min-w-0">
                          <a
                            href={`https://github.com/${repo.owner}`}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center gap-1 text-gray-400 dark:text-gray-500 hover:text-blue-500 font-mono leading-tight transition-colors break-all"
                          >
                            {repo.owner}
                            {repo.owner_type === "Organization" ? (
                              <svg className="shrink-0 text-purple-400 dark:text-purple-500" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-label="Organization">
                                <path d="M3 21V7l9-4 9 4v14"/><path d="M9 21V12h6v9"/><path d="M3 7h18"/>
                              </svg>
                            ) : (
                              <svg className="shrink-0 text-gray-300 dark:text-gray-600" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-label="User">
                                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>
                              </svg>
                            )}
                          </a>
                          <span className="flex items-center gap-1">
                            <a
                              href={repo.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="font-semibold text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 leading-tight transition-colors group-hover:underline"
                              style={{ overflowWrap: "anywhere" }}
                            >
                              {repo.name.split("-").join("-​")}
                            </a>
                            {repo.owner_country && (
                              <span
                                className="text-sm leading-none shrink-0"
                                title={repo.owner_country}
                                aria-label={repo.owner_country}
                              >
                                {countryFlag(repo.owner_country)}
                              </span>
                            )}
                          </span>
                          {isStale && (
                            <span
                              className="block text-[9px] font-mono text-gray-300 dark:text-gray-600 leading-tight"
                              title={`Stats from ${repo.scraped_date} — skipped in latest run`}
                            >
                              {repo.scraped_date}
                            </span>
                          )}
                        </div>
                      </div>
                    </td>
                    <td className="px-2 py-2 text-right font-mono text-gray-800 dark:text-gray-200 font-medium overflow-hidden">
                      {fmt(repo.stars)}
                    </td>
                    <td className="px-2 py-2 text-right font-mono overflow-hidden">
                      <DeltaBadge delta={repo.delta_7d} />
                    </td>
                    <td className="px-2 py-2 text-right font-mono overflow-hidden">
                      <DeltaBadge delta={repo.delta_30d} />
                    </td>
                    <td className="px-2 py-2 text-right font-mono text-gray-500 dark:text-gray-400 overflow-hidden">
                      {fmt(repo.forks)}
                    </td>
                    <td className="px-2 py-2 text-right font-mono text-gray-500 dark:text-gray-400 overflow-hidden">
                      {repo.contributors != null ? fmt(repo.contributors) : <span className="text-gray-300 dark:text-gray-600">—</span>}
                    </td>
                    <td className="px-2 py-2">
                      <DescriptionCell text={repo.description} />
                    </td>
                    <td className="px-2 py-2 overflow-hidden">
                      <div className="flex flex-col gap-1">
                        {catSlugs.map((cs) => {
                          const cat = CATEGORIES.find((c) => c.slug === cs);
                          if (!cat) return null;
                          return <CategoryPill key={cs} categorySlug={cs} categoryName={cat.category} />;
                        })}
                      </div>
                    </td>
                    <td className="px-2 py-2 overflow-hidden">
                      <div className="flex flex-col gap-1">
                        {repo.tags.map((t) => <TagPill key={t} tag={t} />)}
                      </div>
                    </td>
                    <td className="px-2 py-2 text-right font-mono text-gray-500 dark:text-gray-400 overflow-hidden">
                      {fmt(repo.issues)}
                    </td>
                    <td className="px-2 py-2 text-gray-400 dark:text-gray-500 overflow-hidden">
                      {repo.primary_language ?? "—"}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {/* Pagination footer */}
      {totalPages > 1 && (
        <div className="flex items-center justify-between mt-4">
          <p className="text-xs text-gray-400 dark:text-gray-500">
            Showing {(page * pageSize + 1).toLocaleString()}–{Math.min((page + 1) * pageSize, sorted.length).toLocaleString()} of {sorted.length.toLocaleString()}
          </p>
          <div className="flex items-center gap-1">
            <button
              onClick={() => setPage(0)}
              disabled={page === 0}
              className="px-2 py-1 rounded text-xs border border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 disabled:opacity-30 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
            >
              «
            </button>
            <button
              onClick={() => setPage((p) => Math.max(0, p - 1))}
              disabled={page === 0}
              className="px-2 py-1 rounded text-xs border border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 disabled:opacity-30 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
            >
              ‹ Prev
            </button>
            {Array.from({ length: totalPages }, (_, i) => i)
              .filter((i) => Math.abs(i - page) <= 2 || i === 0 || i === totalPages - 1)
              .reduce<(number | "…")[]>((acc, i, idx, arr) => {
                if (idx > 0 && i - (arr[idx - 1] as number) > 1) acc.push("…");
                acc.push(i);
                return acc;
              }, [])
              .map((item, idx) =>
                item === "…" ? (
                  <span key={`ellipsis-${idx}`} className="px-1 text-xs text-gray-400 dark:text-gray-600">…</span>
                ) : (
                  <button
                    key={item}
                    onClick={() => setPage(item as number)}
                    className={`px-2 py-1 rounded text-xs border transition-colors ${
                      page === item
                        ? "bg-gray-800 dark:bg-gray-200 text-white dark:text-gray-900 border-gray-800 dark:border-gray-200"
                        : "border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800"
                    }`}
                  >
                    {(item as number) + 1}
                  </button>
                )
              )}
            <button
              onClick={() => setPage((p) => Math.min(totalPages - 1, p + 1))}
              disabled={page === totalPages - 1}
              className="px-2 py-1 rounded text-xs border border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 disabled:opacity-30 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
            >
              Next ›
            </button>
            <button
              onClick={() => setPage(totalPages - 1)}
              disabled={page === totalPages - 1}
              className="px-2 py-1 rounded text-xs border border-gray-200 dark:border-gray-700 text-gray-500 dark:text-gray-400 disabled:opacity-30 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
            >
              »
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
