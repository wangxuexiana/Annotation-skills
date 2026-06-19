#!/usr/bin/env python3
"""Append live rule, style, quiz, or manual updates to a task skill."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


TARGETS = {
    "audit": "references/pre-submit-audit.md",
    "checklist": "references/decision-checklist.md",
    "failure": "references/common-failure-patterns.md",
    "rule": "references/rule-updates.md",
    "priority": "references/priority-rules.md",
    "pattern": "references/learned-patterns.md",
    "style": "references/user-style.md",
    "reason": "references/reason-examples.md",
    "quiz": "references/quiz-draft.md",
    "manual": "references/manual-summary.md",
}


CORRECTION_TARGETS = {
    "audit": "audit",
    "checklist": "checklist",
    "failure": "failure",
    "manual": "manual",
    "override": "rule",
    "priority": "priority",
    "reason": "reason",
    "rule": "pattern",
    "style": "style",
}


def read_update(args: argparse.Namespace) -> str:
    if args.from_correction_log:
        raise SystemExit("--from-correction-log cannot be combined with --text or --file")
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


def parse_correction_entries(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    text_lines: list[str] = []
    in_text = False
    in_comment = False

    def flush() -> None:
        nonlocal current, text_lines, in_text
        if current is not None:
            current["text"] = "\n".join(text_lines).strip()
            entries.append(current)
        current = None
        text_lines = []
        in_text = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if stripped.startswith("<!--"):
            in_comment = True
        if in_comment:
            if stripped.endswith("-->") or "-->" in stripped:
                in_comment = False
            continue
        if line.startswith("### "):
            flush()
            current = {"title": line[4:].strip(), "type": "", "source": ""}
            continue
        if current is None:
            continue
        if line.startswith("Type:"):
            current["type"] = line.split(":", 1)[1].strip().lower()
            in_text = False
            continue
        if line.startswith("Source:"):
            current["source"] = line.split(":", 1)[1].strip()
            in_text = False
            continue
        if line.startswith("Text:"):
            in_text = True
            remainder = line.split(":", 1)[1].strip()
            if remainder:
                text_lines.append(remainder)
            continue
        if in_text:
            text_lines.append(line)

    flush()
    return entries


def append_entry(path: Path, title: str, text: str, source: str | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(f"# {path.stem.replace('-', ' ').title()}\n", encoding="utf-8")
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    source_line = f"\nSource: {source}" if source else ""
    entry = f"\n\n## {now} - {title}{source_line}\n\n{text}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def append_correction_log(skill_dir: Path, correction_log: Path) -> int:
    if not correction_log.exists():
        raise SystemExit(f"missing correction log: {correction_log}")

    entries = parse_correction_entries(correction_log.read_text(encoding="utf-8-sig"))
    merged = 0
    skipped: list[str] = []

    for entry in entries:
        correction_type = entry["type"]
        title = entry["title"] or "Correction log entry"
        text = entry["text"]
        source = entry["source"] or "state/corrections.md"

        if not text:
            skipped.append(f"{title}: empty Text block")
            continue
        if correction_type == "one-off":
            skipped.append(f"{title}: one-off corrections are not merged into long-term references")
            continue
        target = CORRECTION_TARGETS.get(correction_type)
        if not target:
            skipped.append(f"{title}: unknown Type {correction_type!r}")
            continue

        append_entry(skill_dir / TARGETS[target], title, text, source)
        merged += 1

    print(f"merged {merged} correction(s)")
    for item in skipped:
        print(f"skipped: {item}")
    return merged


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
    parser.add_argument(
        "--from-correction-log",
        nargs="?",
        const="state/corrections.md",
        help="Merge reusable entries from a corrections log. Defaults to state/corrections.md.",
    )
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"not a skill directory: {skill_dir}")

    if args.from_correction_log:
        correction_log = Path(args.from_correction_log)
        if not correction_log.is_absolute():
            correction_log = skill_dir / correction_log
        append_correction_log(skill_dir, correction_log)
        print("next: validate the skill with quick_validate.py")
        return

    update = read_update(args)
    target_path = skill_dir / TARGETS[args.target]
    append_entry(target_path, args.title, update, args.source)
    print(f"updated {target_path}")
    print("next: validate the skill with quick_validate.py")


if __name__ == "__main__":
    main()
