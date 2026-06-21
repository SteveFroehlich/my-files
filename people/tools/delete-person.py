#!/usr/bin/env python3
"""Remove a person from people-index.csv and delete their directory."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

PEOPLE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = PEOPLE_DIR / "people-index.csv"

USAGE_EXAMPLE = """\
Example:
  python people/tools/delete-person.py --person-id p004

  python people/tools/delete-person.py --person-id p003 --dry-run

  python people/tools/delete-person.py --person-id p001 --csv-only

Required:
  --person-id   person_id from people-index.csv (e.g. p001)

Optional:
  --csv-only    Remove the CSV row only; leave any on-disk directory in place
  --dry-run     Print planned deletions without changing files
"""


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


def slugify(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def resolve_person_dir(row: dict[str, str]) -> Path | None:
    snapshot_path = (row.get("snapshot_path") or "").strip()
    if snapshot_path:
        person_dir = (PEOPLE_DIR.parent / snapshot_path).resolve().parent
    else:
        name = (row.get("name") or "").strip()
        slug = slugify(name)
        if not slug:
            return None
        person_dir = (PEOPLE_DIR / slug).resolve()

    try:
        person_dir.relative_to(PEOPLE_DIR.resolve())
    except ValueError:
        fail(f"Refusing to delete path outside people/: {person_dir}")

    return person_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Remove a person from people-index.csv and delete their snapshot directory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=USAGE_EXAMPLE,
    )
    parser.add_argument("--person-id", help="person_id from people-index.csv")
    parser.add_argument(
        "--csv-only",
        action="store_true",
        help="Remove the CSV row only; do not delete any on-disk directory",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show planned deletions without writing")
    return parser


def fail(message: str) -> None:
    print(f"Error: {message}\n", file=sys.stderr)
    print(USAGE_EXAMPLE, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.person_id:
        fail("Missing required argument: --person-id")

    if not CSV_PATH.exists():
        fail(f"CSV not found: {CSV_PATH}")

    fieldnames, rows = read_csv_rows()
    if not fieldnames:
        fail(f"CSV has no header row: {CSV_PATH}")

    row = find_row(rows, args.person_id)
    if row is None:
        fail(f"--person-id {args.person_id!r} not found in {CSV_PATH}")

    person_dir = resolve_person_dir(row)
    directory_exists = person_dir is not None and person_dir.is_dir()

    print(f"person_id:      {args.person_id}")
    print(f"name:           {row.get('name', '')}")
    print(f"csv row:        {row}")
    if person_dir is not None:
        print(f"directory:      {person_dir}")
        print(f"dir exists:     {directory_exists}")
    else:
        print("directory:      (none resolved)")

    if args.csv_only:
        print("mode:           csv-only")
    elif directory_exists:
        print("mode:           csv row + directory")
    else:
        print("mode:           csv row only (no directory on disk)")

    if args.dry_run:
        print("\nDry run — no files deleted.")
        return

    remaining_rows = [candidate for candidate in rows if candidate.get("person_id") != args.person_id]
    if len(remaining_rows) == len(rows):
        fail(f"--person-id {args.person_id!r} not found in {CSV_PATH}")

    write_csv_rows(fieldnames, remaining_rows)

    if not args.csv_only and directory_exists and person_dir is not None:
        shutil.rmtree(person_dir)

    print("\nPerson deleted successfully.")


if __name__ == "__main__":
    main()
