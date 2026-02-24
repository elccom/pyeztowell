from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple


def _run(command: List[str], dry_run: bool = False) -> str:
    if dry_run:
        print("[dry-run]", " ".join(command))
        return ""
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    return completed.stdout.strip()


def _parse_version(version: str) -> Tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        raise ValueError(f"유효하지 않은 버전 형식: {version}")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def _bump_version(current: str, bump: str) -> str:
    major, minor, patch = _parse_version(current)
    if bump == "major":
        return f"{major + 1}.0.0"
    if bump == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def _read_current_version(pyproject_path: Path) -> str:
    content = pyproject_path.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"\s*$', content, flags=re.MULTILINE)
    if not match:
        raise ValueError("pyproject.toml에서 version 항목을 찾지 못했습니다.")
    return match.group(1)


def _update_pyproject_version(pyproject_path: Path, next_version: str) -> None:
    content = pyproject_path.read_text(encoding="utf-8")
    updated = re.sub(
        r'(^version\s*=\s*")([0-9]+\.[0-9]+\.[0-9]+)("\s*$)',
        rf"\\g<1>{next_version}\\g<3>",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    pyproject_path.write_text(updated, encoding="utf-8")


def _get_changed_files(dry_run: bool = False) -> List[str]:
    if dry_run:
        return []
    raw = _run(["git", "status", "--porcelain"], dry_run=False)
    files: List[str] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", maxsplit=1)[1]
        files.append(path)
    return sorted(set(files))


def _update_release_notes(
    release_notes_path: Path,
    version: str,
    changed_files: List[str],
    summary_items: List[str],
) -> None:
    today = dt.date.today().isoformat()

    lines: List[str] = []
    lines.append(f"## v{version} ({today})")
    lines.append("")
    lines.append("### 변경 사항")
    for item in summary_items:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("### 변경 파일")
    if changed_files:
        for file_path in changed_files:
            lines.append(f"- `{file_path}`")
    else:
        lines.append("- (변경 파일 없음)")
    lines.append("")

    new_section = "\n".join(lines)

    if release_notes_path.exists():
        original = release_notes_path.read_text(encoding="utf-8")
    else:
        original = "# Release Notes\n\n"

    if not original.startswith("# Release Notes"):
        original = "# Release Notes\n\n" + original

    header = "# Release Notes\n\n"
    body = original[len(header) :] if original.startswith(header) else original
    updated = header + new_section + body.lstrip("\n")
    release_notes_path.write_text(updated, encoding="utf-8")


def _commit_tag_push(
    version: str,
    commit_message: Optional[str],
    remote: str,
    branch: str,
    dry_run: bool,
) -> None:
    message = commit_message or f"chore: release v{version}"
    tag_name = f"v{version}"

    _run(["git", "add", "pyproject.toml", "RELEASE_NOTES.md"], dry_run=dry_run)
    _run(["git", "commit", "-m", message], dry_run=dry_run)
    _run(["git", "tag", tag_name], dry_run=dry_run)
    _run(["git", "push", remote, branch], dry_run=dry_run)
    _run(["git", "push", remote, tag_name], dry_run=dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description="다음 버전 릴리스를 자동화합니다.")
    parser.add_argument("--version", help="직접 지정할 버전 (예: 0.1.2)")
    parser.add_argument("--bump", choices=["patch", "minor", "major"], default="patch", help="자동 증가 방식")
    parser.add_argument("--summary", action="append", default=[], help="릴리스 요약 항목(여러 번 지정 가능)")
    parser.add_argument("--message", help="커밋 메시지")
    parser.add_argument("--remote", default="origin", help="push 대상 remote")
    parser.add_argument("--branch", default="main", help="push 대상 브랜치")
    parser.add_argument("--dry-run", action="store_true", help="실제 git 작업 없이 실행 계획만 출력")
    args = parser.parse_args()

    project_root = Path.cwd()
    pyproject_path = project_root / "pyproject.toml"
    release_notes_path = project_root / "RELEASE_NOTES.md"

    current_version = _read_current_version(pyproject_path)
    next_version = args.version or _bump_version(current_version, args.bump)

    if not args.summary:
        summary_items = ["버전 업데이트 및 릴리스 반영"]
    else:
        summary_items = args.summary

    changed_files = _get_changed_files(dry_run=args.dry_run)

    if args.dry_run:
        print(f"[dry-run] current={current_version}, next={next_version}")
        print(f"[dry-run] changed_files={changed_files}")
        print("[dry-run] update pyproject.toml and RELEASE_NOTES.md")
        _commit_tag_push(
            version=next_version,
            commit_message=args.message,
            remote=args.remote,
            branch=args.branch,
            dry_run=True,
        )
        print(f"Release completed: v{next_version}")
        return

    _update_pyproject_version(pyproject_path, next_version)
    _update_release_notes(
        release_notes_path=release_notes_path,
        version=next_version,
        changed_files=changed_files,
        summary_items=summary_items,
    )

    _commit_tag_push(
        version=next_version,
        commit_message=args.message,
        remote=args.remote,
        branch=args.branch,
        dry_run=False,
    )

    print(f"Release completed: v{next_version}")


if __name__ == "__main__":
    main()
