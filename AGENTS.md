# AGENTS.md

Instructions for AI coding agents working in this repository. For a human-oriented topic map, see [README.md](README.md).

This is a **personal information system** (Markdown notes and CSV indexes), not an application codebase. There are no build, test, or deploy steps. Agents should read targeted files, edit only what the task requires, and avoid inventing structure or content.

---

## Bootstrap: starting with zero context

When you have no prior knowledge of this repo, follow this order:

1. Read [README.md](README.md) for the high-level topic map.
2. Read this file (`AGENTS.md`) for workflows, conventions, and what not to do.
3. Identify which **domain** the user's task belongs to (people, growth, logs, health, travel, little-humans, Grainger, agent-setup).
4. Open the **nearest domain readme** if one exists (e.g. [people/Readme.md](people/Readme.md), [growth/topics-reference/Readme.md](growth/topics-reference/Readme.md)).
5. Use `grep` or repository search to find relevant prose; there is **no global content index**.
6. Do **not** read `private-data/` unless the user explicitly asks you to work with those files.

---

## Project overview

- **Purpose:** Capture and retrieve personal knowledge for humans and machines—relationships, learning and writing, health, travel, family/parenting, journals, and work context (Grainger).
- **Primary formats:** Markdown with YAML front matter; [people/people-index.csv](people/people-index.csv) for cross-person operational queries.
- **Scale:** Small repo (~55 tracked content files). Prefer reading specific files over broad refactors, new indexes, or automation unless the user requests it.
- **Tooling:** Obsidian is used locally (`.obsidian/` is gitignored). Do not edit `.obsidian/` as part of routine tasks.

---

## Repository layout

Use **lowercase** directory names in paths and links where possible (`growth/`, `logs/`, `travel/`, `people/`). macOS may treat paths as case-insensitive; Linux and git on Linux do not. The work folder is tracked in git as `Grainger/` (capital G).

| Path | Role |
|------|------|
| [people/](people/) | Relationship management: snapshots, interactions, CSV index, helper scripts |
| [growth/](growth/) | Learning, writing, reference material, and inbox scrapes |
| [logs/](logs/) | Journals: daily, weekly, quarterly, and year-end reviews |
| [health/](health/) | Health notes, routines, grocery, medical history |
| [travel/](travel/) | Travel planning and checklists |
| [little-humans/](little-humans/) | Parenting notes and kids' activities |
| [Grainger/](Grainger/) | Work-related notes (matching, tools to explore) |
| [agent-setup/](agent-setup/) | Agent tooling and home-lab infrastructure plans |
| [scripts-repo-level/](scripts-repo-level/) | Utility shell scripts for repo metrics (not domain content) |
| `private-data/` | **Out of git.** Sensitive notes; see [Security](#security) |

### growth/ subtree

| Path | Role |
|------|------|
| [growth/scrapes/](growth/scrapes/) | **Inbox** — raw links and notes by topic; not canonical |
| [growth/books/](growth/books/) | Book notes |
| [growth/content/](growth/content/) | Writing pipeline (ideas → drafts → completed) |
| [growth/content/raw-content-ideas.md](growth/content/raw-content-ideas.md) | Inbox for content ideas and fragments |
| [growth/content/short-form/](growth/content/short-form/) | Short-form pieces in progress |
| [growth/content/long-form/](growth/content/long-form/) | Long-form pieces in progress |
| [growth/content/completed-content/](growth/content/completed-content/) | Finished / published content |
| [growth/form-understanding/](growth/form-understanding/) | **Active deep dives** — day-by-day exploration while forming understanding |
| [growth/topics-reference/](growth/topics-reference/) | **Long-term reference** — distilled notes to return to after a deep dive is done |
| [growth/high-signal-sources.md](growth/high-signal-sources.md) | Curated external sources worth following |
| [growth/custom-software-wish-list.md](growth/custom-software-wish-list.md) | Software ideas and feature sketches |

**form-understanding vs topics-reference:** These are different stages of learning, not interchangeable.

- **`form-understanding/`** — Use while actively deep-diving on something day by day. Messy notes, experiments, and work-in-progress understanding belong here (e.g. `ai-native-software.md`, `ai-core-concepts.md`).
- **`topics-reference/`** — Use for long-term topics you want to grow in. After a deep dive is complete, promote the distilled reference material here so you can revisit it later to keep understanding current (e.g. `communication/linguistics.md`, `communication/dictionary.md`).

When promoting from active exploration to reference: summarize and distill in `topics-reference/`; do not copy large raw blocks. Remove or trim the source in `form-understanding/` once the reference version is canonical.

### growth/scrapes/ files (inbox, not canonical)

Each file is a topic-specific holding area. Do not treat these as source of truth.

| File | Typical content |
|------|-----------------|
| `book-scrapes.md` | Books to read or quick notes |
| `digital-art-scrapes.md` | Digital art links and ideas |
| `finance-scrapes.md` | Finance links and notes |
| `fitness-scrapes.md` | Fitness links and notes |
| `health-scrapes.md` | Health links and notes |
| `little-human-scrapes.md` | Parenting / kids links and ideas |
| `people-scrapes.md` | People not yet promoted to a full person folder |
| `science-scrapes.md` | Science links and notes |
| `tech-scrapes.md` | Tech links, talks, articles |

When promoting a scrape item: move or summarize it into the appropriate curated location (book note, topics-reference, form-understanding, high-signal-sources, etc.). Do not duplicate large scrape blocks across files. Once curated, remove it from the scrape file.

---

## How to navigate by task type

| Task | Start here |
|------|------------|
| People triage (“who to contact,” follow-ups, status) | [people/people-index.csv](people/people-index.csv) → each person's `snapshot_path` |
| Working on one person | `{slug}/{slug}-snapshot.md` → `interactions/` |
| Finding prose across the repo | `grep` / repository search (no global index) |
| Promoting a link or raw note | Identify domain → move to curated file → remove from scrape/inbox |
| Writing content | `raw-content-ideas.md` → `short-form/` or `long-form/` (WIP) → `completed-content/` |
| Active learning / deep dive | `form-understanding/` |
| Stable reference after a deep dive | `topics-reference/` |
| Domain schema and enums | Nearest readme (e.g. [people/Readme.md](people/Readme.md)) |

---

## People workflow

Detailed schema and enums: [people/Readme.md](people/Readme.md).

This system answers: who matters, when did I last interact, what follow-ups exist, what context to remember, and whether sensitive detail lives elsewhere.

### Directory structure

```
people/
  people-index.csv
  Readme.md
  _templates/
    person-snapshot-template.md
    person-interaction-template.md
  scripts/
    add-person.py
    delete-person.py
  {kebab-slug}/
    {kebab-slug}-snapshot.md
    interactions/
      {YYYY-MM-DD}-{kebab-slug}.md   # match existing naming in that folder if it differs
```

### Read order

1. `people/people-index.csv` — operational view (status, dates, paths, tags).
2. `{slug}/{slug}-snapshot.md` — durable context and open loops.
3. `{slug}/interactions/` — one file per interaction; when comparing dates, newest first.

### Real people vs schema examples

Verify paths before reading. Every `snapshot_path` in the CSV should exist on disk for real contacts.

| person_id | Name | On disk? | Notes |
|-----------|------|----------|-------|
| p001 | Kait Sweetman | Yes — `people/kait-sweetman/` | Real contact |
| p002 | Jane Doe | **No** — folder does not exist | **Schema example only**; do not invent this folder or history |
| p003 | Henry Beardsley | Yes — `people/henry-beardsley/` | Real contact; `interactions/` exists but may be empty |

Do not invent people, CSV rows, interaction files, or assume every CSV row is a real contact.

### People inbox

People who are not yet full person folders live in [growth/scrapes/people-scrapes.md](growth/scrapes/people-scrapes.md) (not under `people/`).

Do not add CSV rows or person directories from scrapes unless the user asks.

### Creating or updating people

Use templates in [people/_templates/](people/_templates/):

- **New person:** copy `person-snapshot-template.md` → `people/{kebab-slug}/{kebab-slug}-snapshot.md`
- **New interaction:** copy `person-interaction-template.md` → `people/{kebab-slug}/interactions/{filename}.md` (match existing files in that folder if the pattern differs)

Or use the helper script (preferred for new people):

```bash
python people/scripts/add-person.py --name "Full Name" --category professional
python people/scripts/add-person.py --dry-run --name "Full Name" --category friend
```

Run with missing required flags to print usage. `add-interaction.py` is **not implemented** — create interaction files from the template and sync snapshot + CSV manually.

**Front matter (snapshots):** `person_id`, `name`, `category`, `priority`, `preferred_channel`, `acquired_from`, `last_contacted`, `next_follow_up` (snapshots may also include `email`, `phone`, etc.)

**Front matter (interactions):** `person_id`, `date`, `interaction_type` — one of: `email`, `text`, `video-call`, `phone-call`, `in-person`, `group-event`

**CSV columns:** See header in `people-index.csv`.

- `status`: `in_circle`, `engaged`, `following`, `dormant`
- `target_frequency`: `as-needed`, `monthly`, `weekly`, `quarterly`
- `category`: e.g. `friend`, `professional`, `colleague`
- `has_sensitive_snapshot`: if `true`, detailed sensitive notes may live outside this repo

### Keep index and snapshots in sync

After adding or editing an interaction:

1. Set `date` in the interaction file front matter.
2. Update `last_contacted` (and `next_follow_up` if applicable) in the person snapshot front matter.
3. Update the matching row in `people-index.csv` (`last_contacted`, `next_follow_up`, `status` as needed).

**Source of truth:** CSV for cross-person queries and weekly triage; snapshot front matter for detail when working on one person. If they conflict, prefer the **newest interaction file** and fix the CSV and snapshot to match.

### Sensitive context

If `has_sensitive_snapshot` is `true`, detailed sensitive notes may live outside this repo (`private-data/` or encrypted storage). Do not infer or fabricate sensitive content. Non-sensitive summaries belong in the snapshot.

---

## Growth workflow

### Content pipeline

Writing moves through stages. Do not treat earlier stages as canonical once promoted.

| Stage | Location | Purpose |
|-------|----------|---------|
| Ideas inbox | `growth/content/raw-content-ideas.md` | Fragments, outlines, quotes, prompts |
| Short-form WIP | `growth/content/short-form/` | Shorter pieces in progress |
| Long-form WIP | `growth/content/long-form/` | Longer pieces in progress |
| Completed | `growth/content/completed-content/` | Finished or published pieces |

When a piece is done, move it to `completed-content/`. Do not leave duplicate full copies in inbox or draft locations. Do not put active drafts at `growth/content/` root—use `short-form/` or `long-form/` instead.

Current examples:

- **Completed:** `giving-tree-inscription-cara.md`, `outcome-based-performance-reviews.md`, `what-a-good-team-feels-like.md`
- **Short-form (in progress):** `placeholder.md`
- **Long-form (in progress):** `future-of-documentation.md`, `matching-roadmap-experiment.md`

### Books

Book notes live in [growth/books/](growth/books/). Filename conventions vary (e.g. `beginning-of-infinity.md`, `Never split the difference.md`); match siblings when adding new notes.

### Curated sources and wish lists

- [growth/high-signal-sources.md](growth/high-signal-sources.md) — external people and sites worth following
- [growth/custom-software-wish-list.md](growth/custom-software-wish-list.md) — software product sketches

---

## Logs

- **Path:** [logs/](logs/)
- **Daily:** `logs/Daily/` — prefer `YYYY-MM-DD` in new daily filenames when creating files (existing file: `Daily log 2026-04-26.md`)
- **Weekly:** `logs/Weekly/` — reserved; may be empty
- **Quarterly:** `logs/Quarterly/` — reserved; may be empty
- **Year-end:** `logs/end-of-year-review-*.md` at `logs/` root (e.g. `end-of-year-review-2025.md`)

Match the style and section headings of neighboring log files when adding entries.

---

## Health

- **Path:** [health/](health/)
- **Topics on disk:** daily routine, emotional health, head health, healthy drinks, grocery, medical history
- **Medical history:** `health/medical-history/` (e.g. `Incidents 2026.md`)
- Filename conventions vary; match siblings in the same folder when creating files

---

## Travel

- **Path:** [travel/](travel/)
- **Current file:** `travel-checklist.md`
- Travel planning and reference notes; match existing style when adding files

---

## little-humans

- **Path:** [little-humans/](little-humans/)
- Parenting notes and kids' activities
- **On disk:**
  - `raising-little-humas.md` — parenting notes (filename retains typo "humas")
  - `activities-little-humans/` — activity lists and individual activity notes (e.g. `paddle-boating.md`)
- Related scrape inbox: [growth/scrapes/little-human-scrapes.md](growth/scrapes/little-human-scrapes.md)

Do not rename `raising-little-humas.md` unless the user asks.

---

## Grainger (work)

- **Path:** [Grainger/](Grainger/) (capital G in git)
- Work-related notes, not personal relationship management
- **On disk:** `Matching.md`, `Tools to explore.md`

---

## agent-setup

- **Path:** [agent-setup/](agent-setup/)
- Agent tooling and home-lab infrastructure plans (hardware architecture, voice, two-machine split, etc.)
- **File:** `agent-setup.md` — can be long; do not load full hardware specs when the task is about people, health, or notes unless the user asks

---

## Scripts

### people/scripts/

Python CLI helpers. All support `--dry-run`. Missing required flags prints usage.

| Script | Purpose |
|--------|---------|
| `add-person.py` | Create person folder, snapshot, and CSV row. Requires `--name`, `--category`. |
| `delete-person.py` | Remove CSV row and on-disk folder. Requires `--person-id`; `--csv-only` keeps files. |

### scripts-repo-level/

Utility shell scripts for repo metrics (file counts, sizes, line counts). Not part of domain workflows. Do not run or modify unless the user asks.

| Script | Purpose |
|--------|---------|
| `count_lines.sh` | Line counts |
| `count_size_files_only.sh` | File sizes (files only) |
| `count_size_dirs_and_files.sh` | Directory and file sizes |

---

## File and editing conventions

- **Paths:** Lowercase top-level folders where possible; `kebab-case` for person directory slugs (e.g. `kait-sweetman`, `henry-beardsley`).
- **Changes:** Only modify files required by the task. No drive-by refactors, renames, or new indexes unless requested.
- **Commits:** Do not commit unless the user explicitly asks.
- **Markdown:** Match the style and section headings of neighboring files and templates.
- **New top-level folders:** Do not create without user direction.
- **Front matter:** Preserve YAML front matter structure when editing people files; keep CSV and snapshot dates aligned after interaction changes.

---

## Security

- **`private-data/`** is listed in `.gitignore`. Do not read, search, or summarize files there unless the user explicitly includes them in the task.
- Never commit secrets, credentials, or contents from `private-data/`.
- Do not echo sensitive personal data into chat unless the user needs it for the task at hand.
- Several people have `has_sensitive_snapshot: true`; treat snapshot bodies as non-sensitive summaries only.

---

## What not to do

- Invent people, CSV rows, or interaction history.
- Assume every row in `people-index.csv` represents a real on-disk person folder (p002 Jane Doe is an example only).
- Merge or “clean up” scrape inboxes without explicit instruction.
- Add repo-wide indexes, databases, or automation unless the user requests it.
- Edit `private-data/` or `.obsidian/` as part of routine tasks.
- Duplicate large scrape or draft blocks across multiple canonical locations.
- Promote scrape items to person folders or CSV without user direction.
- Confuse `form-understanding/` (active deep dive) with `topics-reference/` (stable reference after the dive).

---

## Nested instructions

If a subtree gains its own `AGENTS.md` later (e.g. `people/AGENTS.md`), the closest `AGENTS.md` to the edited file takes precedence for that subtree. Until then, this file plus domain readmes define conventions:

- [people/Readme.md](people/Readme.md) — people schema, scripts, enums
- [growth/topics-reference/Readme.md](growth/topics-reference/Readme.md) — reference vs active learning
