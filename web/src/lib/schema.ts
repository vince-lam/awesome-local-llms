import { sqliteTable, text, integer, index, uniqueIndex } from "drizzle-orm/sqlite-core";
import { sql } from "drizzle-orm";

export const repos = sqliteTable("repos", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  fullName: text("full_name").notNull().unique(),
  owner: text("owner").notNull(),
  name: text("name").notNull(),
  description: text("description"),
  url: text("url").notNull(),
  tags: text("tags").notNull().default("[]"),
  platforms: text("platforms").notNull().default("[]"),
  backends: text("backends").notNull().default("[]"),
  ownerType: text("owner_type"),
  addedAt: text("added_at").notNull().default(sql`(date('now'))`),
});

export const snapshots = sqliteTable(
  "snapshots",
  {
    id: integer("id").primaryKey({ autoIncrement: true }),
    repoId: integer("repo_id")
      .notNull()
      .references(() => repos.id),
    scrapedDate: text("scraped_date").notNull(),
    stars: integer("stars").notNull().default(0),
    forks: integer("forks").notNull().default(0),
    issues: integer("issues").notNull().default(0),
    releases: integer("releases"),
    watchers: integer("watchers").notNull().default(0),
    daysSinceCommit: integer("days_since_commit"),
    license: text("license"),
    primaryLanguage: text("primary_language"),
    contributors: integer("contributors"),
  },
  (table) => ({
    repoDateIdx: uniqueIndex("repo_date_idx").on(table.repoId, table.scrapedDate),
    dateIdx: index("date_idx").on(table.scrapedDate),
    starsIdx: index("stars_idx").on(table.stars),
  })
);
