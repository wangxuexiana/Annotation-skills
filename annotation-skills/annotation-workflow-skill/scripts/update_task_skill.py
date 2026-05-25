#!/usr/bin/env python3
"""Append live rule, style, quiz, or manual updates to a task skill."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


TARGETS = {
    "rule": "references/rule-updates.md",
    "pattern": "references/learned-patterns.md",
    "style": "references/user-style.md",
    "reason": "references/reason-examples.md",
    "quiz": "references/quiz-draft.md",
    "manual": "references/manual-summary.md",
}


def read_update(args: argparse.Namespace) -> str:
    if args.text and args.file:
        raise SystemExit("pass either --text or --file, not both")
    if args.file:
        path = Path(args.file)
        if not path.exists():
            raise SystemExit(f"missing update file: {path}")
        text = path.read_text(encoding="utf-8-sig")
    elif args.text:
        text = args.text
    else:
        raise SystemExit("pass --text or --file")
    text = text.strip()
    if not text:
        raise SystemExit("update text is empty")
    return text


def append_entry(path: Path, title: str, text: str, source: str | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(f"# {path.stem.replace('-', ' ').title()}\n", encoding="utf-8")
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    source_line = f"\nSource: {source}" if source else ""
    entry = f"\n\n## {now} - {title}{source_line}\n\n{text}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", required=True, help="Path to the task skill folder")
    parser.add_argument(
        "--target",
        choices=sorted(TARGETS),
        default="rule",
        help="Which reference file to update",
    )
    parser.add_argument("--title", default="Live update")
    parser.add_argument("--text")
    parser.add_argument("--file")
    parser.add_argument("--source", help="Manual link, user correction, quiz feedback, or other source")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"not a skill directory: {skill_dir}")

    update = read_update(args)
    target_path = skill_dir / TARGETS[args.target]
    append_entry(target_path, args.title, update, args.source)
    print(f"updated {target_path}")
    print("next: validate the skill with quick_validate.py")


if __name__ == "__main__":
    main()
