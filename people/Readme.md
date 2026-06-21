
# Relationship management system

This system answers the questions:
* Who are the important people in my life?
* When did I last interact with them?
* Is there anything I need to follow up on?
* What context do I want to remember before seeing them again?
* What sensitive context needs to be protected separately?

## Schema
```
people/
  people-index.csv
  _templates/
    person-snapshot-template.md
    person-interaction-template.md

  jane-doe/
    jane-doe-snapshot.md
    interactions/
      2026-05-15-in-person-jane-doe.md
      2026-06-15-text-jane-doe.md

  alex-smith/
    alex-smith-snapshot.md
    interactions/
      2026-05-20-video-call-alex-smith.md
```

## Descriptions
`people-scrapes.md` holding area for random people until they can be added or discarded.

`people-index.csv` answers the question what relationship should I invest energy in for the coming week?

Each person gets a directory.

`interactions` directory holds a file for each interaction.

## Tools

CLI helpers in `tools/` (flags only; missing required flags prints usage). All support `--dry-run`.

- **`add-person.py`** — Create person folder, snapshot, and CSV row. Requires `--name`, `--status`; `--category` optional.
- **`delete-person.py`** — Remove CSV row and on-disk folder. Requires `--person-id`; `--csv-only` keeps files.
- **`add-interaction.py`** — Not implemented; create interaction files from `person-interaction-template.md` and sync snapshot + CSV manually.

## Enums

Enums are scoped to the file type where the field lives.

#### interaction.md scoped enums

**interaction_type**
* email
* text
* video-call
* phone-call
* in-person
* group-event

#### snapshot.md scoped enums

**category**
* friend       — personal relationship
* colleague    — someone you work with directly (same company or team)
* family       — relatives
* acquaintance — weaker or newer ties (e.g. met once, pipeline contact)

#### people-index.csv scoped enums

**status** (required by `add-person.py`)
* in_circle
* engaged
* following
* dormant

**category** (optional; same values as snapshot `category`; validated by `add-person.py` when set)
* friend
* colleague
* family
* acquaintance

**target_frequency**
* as-needed
* monthly
* weekly
* quarterly