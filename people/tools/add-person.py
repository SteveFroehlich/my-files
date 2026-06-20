#!/usr/bin/env python3
"""Create a new person directory, snapshot, and CSV row."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

PEOPLE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = PEOPLE_DIR / "people-index.csv"
TEMPLATE_PATH = PEOPLE_DIR / "_templates" / "person-snapshot-template.md"

STATUSES = frozenset({"in_circle", "engaged", "following", "dormant"})
TARGET_FREQUENCIES = frozenset({"as-needed", "monthly", "weekly", "quarterly"})

USAGE_EXAMPLE = """\
Example:
  python people/tools/add-person.py \\
    --name "Henry Beardsley" \\
    --category professional

  python people/tools/add-person.py \\
    --name "Alex Smith" \\
    --category friend \\
    --status in_circle \\
    --priority A \\
    --tags "friend,personal" \\
    --preferred-channel text \\
    --target-frequency monthly

  python people/tools/add-person.py \\
    --person-id p003 \\
    --name "Henry Beardsley" \\
    --category professional \\
    --last-contacted 2026-06-06 \\
    --next-follow-up 2026-06-14

Required:
  --name       Full name (used to derive the directory slug)
  --category   Relationship category (e.g. friend, professional, colleague)

Optional:
  --person-id            Use an existing CSV row id instead of allocating the next one
  --status               in_circle | engaged | following | dormant  (default: following)
  --priority             Priority label (e.g. A, B)
  --target-frequency     as-needed | monthly | weekly | quarterly  (default: as-needed)
  --tags                 Comma-separated tags for the CSV row
  --preferred-channel    e.g. text, email, phone
  --acquired-from        How you met or found this person
  --last-contacted       YYYY-MM-DD
  --next-follow-up       YYYY-MM-DD or "none"
  --has-sensitive-snapshot  true or false  (default: true)
  --dry-run              Print planned changes without writing files
"""


def slugify(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    if not slug:
        raise ValueError(f"Could not derive a slug from name: {name!r}")
    return slug


def yaml_value(value: str) -> str:
    if not value:
        return ""
    if re.search(r'[:#\[\]{}&,*?|>!\'"%@`]', value) or value.strip() != value:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def next_person_id(rows: list[dict[str, str]]) -> str:
    max_num = 0
    for row in rows:
        match = re.fullmatch(r"p(\d+)", row.get("person_id", ""))
        if match:
            max_num = max(max_num, int(match.group(1)))
    return f"p{max_num + 1:03d}"


def read_csv_rows() -> tuple[list[str], list[dict[str, str]]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    return fieldnames, rows


def write_csv_rows(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def find_row(rows: list[dict[str, str]], person_id: str) -> dict[str, str] | None:
    for row in rows:
        if row.get("person_id") == person_id:
            return row
    return None


def render_snapshot(
    *,
    person_id: str,
    name: str,
    category: str,
    priority: str,
    preferred_channel: str,
    acquired_from: str,
    last_contacted: str,
    next_follow_up: str,
) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if not template.startswith("---"):
        raise RuntimeError(f"Snapshot template missing front matter: {TEMPLATE_PATH}")

    _, front_matter, body = template.split("---", 2)
    del front_matter  # structure reference only; snapshot is rendered explicitly

    lines = [
        "---",
        f"person_id: {person_id}",
        f"name: {yaml_value(name)}",
        f"category: {yaml_value(category)}",
    ]
    if priority:
        lines.append(f"priority: {yaml_value(priority)}")
    if preferred_channel:
        lines.append(f"preferred_channel: {yaml_value(preferred_channel)}")
    lines.append(f"acquired_from: {yaml_value(acquired_from)}")
    if last_contacted:
        lines.append(f"last_contacted: {last_contacted}")
    if next_follow_up:
        lines.append(f"next_follow_up: {next_follow_up}")
    lines.append("---")

    snapshot_body = body.replace("# Jane Doe Snapshot", f"# {name} Snapshot", 1)
    return "\n".join(lines) + snapshot_body


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Add a new person to people-index.csv and create their snapshot directory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=USAGE_EXAMPLE,
    )
    parser.add_argument("--name", help="Full name of the person")
    parser.add_argument("--category", help="Relationship category")
    parser.add_argument("--person-id", help="Existing person_id to complete instead of allocating a new one")
    parser.add_argument("--status", help="CSV status (default: following for new rows; preserved for --person-id)")
    parser.add_argument("--priority", help="Priority label")
    parser.add_argument(
        "--target-frequency",
        help="CSV target_frequency (default: as-needed for new rows; preserved for --person-id)",
    )
    parser.add_argument("--tags", help="Comma-separated CSV tags")
    parser.add_argument("--preferred-channel", help="Preferred contact channel")
    parser.add_argument("--acquired-from", help="How you know or found this person")
    parser.add_argument("--last-contacted", help="YYYY-MM-DD")
    parser.add_argument("--next-follow-up", help='YYYY-MM-DD or "none"')
    parser.add_argument(
        "--has-sensitive-snapshot",
        default="true",
        choices=("true", "false"),
        help="Whether sensitive notes may exist outside the repo (default: true)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show planned changes without writing")
    return parser


def fail(message: str) -> None:
    print(f"Error: {message}\n", file=sys.stderr)
    print(USAGE_EXAMPLE, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.name or not args.category:
        missing = []
        if not args.name:
            missing.append("--name")
        if not args.category:
            missing.append("--category")
        fail(f"Missing required argument(s): {', '.join(missing)}")

    if args.status is not None and args.status not in STATUSES:
        fail(f"Invalid --status {args.status!r}. Must be one of: {', '.join(sorted(STATUSES))}")

    if args.target_frequency is not None and args.target_frequency not in TARGET_FREQUENCIES:
        fail(
            f"Invalid --target-frequency {args.target_frequency!r}. "
            f"Must be one of: {', '.join(sorted(TARGET_FREQUENCIES))}"
        )

    if not CSV_PATH.exists():
        fail(f"CSV not found: {CSV_PATH}")

    if not TEMPLATE_PATH.exists():
        fail(f"Snapshot template not found: {TEMPLATE_PATH}")

    slug = slugify(args.name)
    person_dir = PEOPLE_DIR / slug
    snapshot_path = person_dir / f"{slug}-snapshot.md"
    snapshot_path_csv = f"people/{slug}/{slug}-snapshot.md"

    if person_dir.exists():
        fail(f"Person directory already exists: {person_dir}")

    fieldnames, rows = read_csv_rows()
    if not fieldnames:
        fail(f"CSV has no header row: {CSV_PATH}")

    existing_row = find_row(rows, args.person_id) if args.person_id else None
    if args.person_id and existing_row is None:
        fail(f"--person-id {args.person_id!r} not found in {CSV_PATH}")

    if existing_row:
        person_id = args.person_id
        existing_snapshot = (existing_row.get("snapshot_path") or "").strip()
        if existing_snapshot:
            fail(
                f"--person-id {person_id} already has snapshot_path {existing_snapshot!r}. "
                "Refusing to overwrite."
            )
        existing_name = (existing_row.get("name") or "").strip()
        if existing_name and existing_name != args.name:
            fail(
                f"--name {args.name!r} does not match CSV name {existing_name!r} for {person_id}"
            )
    else:
        person_id = next_person_id(rows)
        if find_row(rows, person_id) is not None:
            fail(f"Generated person_id {person_id} already exists in CSV")

    for row in rows:
        row_snapshot = (row.get("snapshot_path") or "").strip()
        if row_snapshot == snapshot_path_csv and row.get("person_id") != person_id:
            fail(f"CSV already references snapshot path {snapshot_path_csv}")

    if existing_row:
        csv_row = dict(existing_row)
        csv_row.update(
            {
                "person_id": person_id,
                "name": args.name,
                "category": args.category,
                "snapshot_path": snapshot_path_csv,
                "has_sensitive_snapshot": args.has_sensitive_snapshot,
            }
        )
        if args.priority is not None:
            csv_row["priority"] = args.priority
        if args.status is not None:
            csv_row["status"] = args.status
        if args.target_frequency is not None:
            csv_row["target_frequency"] = args.target_frequency
        if args.tags is not None:
            csv_row["tags"] = args.tags
        if args.last_contacted is not None:
            csv_row["last_contacted"] = args.last_contacted
        if args.next_follow_up is not None:
            csv_row["next_follow_up"] = args.next_follow_up
    else:
        last_contacted = args.last_contacted or ""
        next_follow_up = args.next_follow_up if args.next_follow_up is not None else ("none" if not last_contacted else "")
        csv_row = {
            "person_id": person_id,
            "name": args.name,
            "category": args.category,
            "priority": args.priority or "",
            "status": args.status or "following",
            "last_contacted": last_contacted,
            "next_follow_up": next_follow_up,
            "target_frequency": args.target_frequency or "as-needed",
            "snapshot_path": snapshot_path_csv,
            "has_sensitive_snapshot": args.has_sensitive_snapshot,
            "tags": args.tags or "",
        }

    snapshot_content = render_snapshot(
        person_id=person_id,
        name=args.name,
        category=args.category,
        priority=args.priority or csv_row.get("priority") or "",
        preferred_channel=args.preferred_channel or "",
        acquired_from=args.acquired_from or "",
        last_contacted=csv_row.get("last_contacted") or "",
        next_follow_up=csv_row.get("next_follow_up") or "",
    )

    print(f"person_id:      {person_id}")
    print(f"slug:           {slug}")
    print(f"directory:      {person_dir}")
    print(f"snapshot:       {snapshot_path}")
    print(f"csv row:        {csv_row}")

    if args.dry_run:
        print("\nDry run — no files written.")
        return

    person_dir.mkdir(parents=False, exist_ok=False)
    (person_dir / "interactions").mkdir()
    snapshot_path.write_text(snapshot_content, encoding="utf-8")

    if existing_row:
        existing_row.update(csv_row)
    else:
        rows.append(csv_row)

    write_csv_rows(fieldnames, rows)
    print("\nPerson added successfully.")


if __name__ == "__main__":
    main()
