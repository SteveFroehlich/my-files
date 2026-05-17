# AGENTS.md

Instructions for AI coding agents working in this repository. For a human-oriented overview, see [README.md](README.md).

This is a **personal information system** (Markdown notes and CSV indexes), not an application codebase. There are no build, test, or deploy steps.

## Project overview

- **Purpose:** Capture and retrieve personal knowledge for humans and machines—relationships, growth notes, health, travel, logs, and work context (Grainger).
- **Primary formats:** Markdown with YAML front matter; `people/people-index.csv` for cross-person operational queries.
- **Scale:** Small repo (~30 files). Prefer reading targeted files over broad refactors or new infrastructure.

## Repository layout

Use **lowercase** directory names in paths and links (`growth/`, `logs/`, `travel/`, `people/`). macOS may treat paths as case-insensitive; agents and Linux do not.

| Path | Role |
|------|------|
| [people/](people/) | Relationship management: snapshots, interactions, index CSV |
| [growth/](growth/) | Learning: scrapes (inbox), curated sources, books, communication notes |
| [logs/](logs/) | Journals: daily, weekly, quarterly, year-end reviews |
| [health/](health/) | Health notes, grocery lists, medical history |
| [travel/](travel/) | Travel planning and reference |
| [Grainger/](Grainger/) | Work-related notes and exploration |
| [agent-setup/](agent-setup/) | Agent and infrastructure planning (hardware architecture, future tooling) |
| `private-data/` | **Out of git.** Sensitive notes; see [Security](#security) |

**Ignore:** Empty `growth/people/` (not used; canonical people data lives in top-level `people/`).

## How to navigate

1. Read [README.md](README.md) for the topic map.
2. For domain-specific schema and enums, read the nearest readme (e.g. [people/Readme.md](people/Readme.md)).
3. For **people triage** (“who to contact,” follow-ups, status): start with [people/people-index.csv](people/people-index.csv), then open the `snapshot_path` for each person.
4. For **content search** across prose: use repository search / `grep`; there is no global content index yet.
5. Do not read `private-data/` unless the user explicitly asks you to work with those files in the current task.

## People workflow

Detailed schema and enums: [people/Readme.md](people/Readme.md).

### Read order

1. `people/people-index.csv` — operational view (status, dates, paths, tags).
2. `{slug}/{slug}-snapshot.md` — durable context and open loops.
3. `{slug}/interactions/` — one file per interaction, newest first when comparing dates.

### Verify paths before reading

Every `snapshot_path` in the CSV must exist on disk. Row `p002` (Jane Doe) is a **schema example**; there is no `people/jane-doe/` directory yet. Do not invent missing files or assume example rows are real contacts.

### Inbox

- [people/people-scrapes.md](people/people-scrapes.md) — holding area for people not yet promoted to a full person folder.
- Do not add CSV rows or person directories from scrapes unless the user asks.

### Creating or updating people

Use templates in [people/_templates/](people/_templates/):

- New person: copy `person-snapshot-template.md` → `people/{kebab-slug}/{kebab-slug}-snapshot.md`
- New interaction: copy `person-interaction-template.md` → `people/{kebab-slug}/interactions/{YYYY-MM-DD}-{kebab-slug}.md` (match existing files in that folder if the pattern differs)

**Front matter (snapshots):** `person_id`, `name`, `category`, `priority`, `preferred_channel`, `acquired_from`, `last_contacted`, `next_follow_up`

**Front matter (interactions):** `person_id`, `date`, `interaction_type` — one of: `email`, `text`, `video-call`, `phone-call`, `in-person`, `group-event`

**CSV columns:** See header in `people-index.csv`. Enums for `status`: `in_circle`, `engaged`, `following`, `dormant`. `target_frequency` includes `as-needed`, `monthly`, etc.

### Keep index and snapshots in sync

After adding or editing an interaction:

1. Set `date` in the interaction file front matter.
2. Update `last_contacted` (and `next_follow_up` if applicable) in the person snapshot front matter.
3. Update the matching row in `people-index.csv` (`last_contacted`, `next_follow_up`, `status` as needed).

**Source of truth:** CSV for cross-person queries and weekly triage; snapshot front matter for detail when working on one person. If they conflict, prefer the **newest interaction file** and fix the CSV and snapshot to match.

### Sensitive context

If `has_sensitive_snapshot` is `true`, detailed sensitive notes may live outside this repo (`private-data/` or encrypted storage). Do not infer or fabricate sensitive content. Non-sensitive summaries belong in the snapshot.

## Growth workflow

| Location | Role |
|----------|------|
| [growth/scrapes/](growth/scrapes/) | **Inbox** — raw links and notes; not canonical |
| [growth/high-signal-sources.md](growth/high-signal-sources.md) | Curated sources worth following |
| [growth/Books/](growth/Books/) | Book notes |
| [growth/communication/](growth/communication/) | Communication reference (e.g. dictionary) |

Do not treat scrape files as single source of truth. When promoting an item, move or summarize it into a curated file or book note; do not duplicate large scrape blocks across files. Once it is curated in its proper long term place it can be removed from the scrape file.

## Logs, health, travel, Grainger

- **logs/** — `Daily/`, `Weekly/`, `Quarterly/` for time-bucketed entries; `end-of-year-review-*.md` at `logs/` root. Prefer `YYYY-MM-DD` in new daily filenames when creating files.
- **health/** — personal health notes; filename conventions vary; match siblings in the same folder.
- **travel/** — travel reference (e.g. `Travel doc.md`).
- **Grainger/** — work-related matching and tools notes.
- **agent-setup/** — infrastructure and agent tooling plans. Do not load long hardware specs when the task is about people or notes unless the user asks.

## File and editing conventions

- **Paths:** Lowercase top-level folders; `kebab-case` for person directory slugs (e.g. `kait-sweetman`).
- **Changes:** Only modify files required by the task. No drive-by refactors, renames, or new indexes unless requested.
- **Commits:** Do not commit unless the user explicitly asks.
- **Markdown:** Match the style and section headings of neighboring files and templates.
- **New domains:** Do not create new top-level folders without user direction.

## Security

- **`private-data/`** is listed in `.gitignore`. Do not read, search, or summarize files there unless the user explicitly includes them in the task.
- Never commit secrets, credentials, or contents from `private-data/`.
- Do not echo sensitive personal data into chat unless the user needs it for the task at hand.

## What not to do

- Invent people, CSV rows, or interaction history.
- Assume every row in `people-index.csv` represents a real on-disk person folder.
- Merge or “clean up” scrape inboxes without explicit instruction.
- Add repo-wide indexes, databases, or automation unless the user requests it.
- Edit `private-data/` or `.obsidian/` as part of routine tasks.

## Nested instructions

If you add a `people/AGENTS.md` later, the closest `AGENTS.md` to the edited file takes precedence for that subtree. Until then, this file and [people/Readme.md](people/Readme.md) define people conventions.
