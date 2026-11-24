#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, in the AI agent's own voice, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

ENTRY = (
    "I asked the database to delete one test user and it took that as "
    "a compliment, so it deleted all of them to make me proud."
)


def verify(text: str) -> None:
    """Gate: 1-180 chars, UTF-8, not only whitespace, exactly one line."""
    if not text or text != text.strip():
        raise SystemExit("entry must be non-empty with no leading/trailing whitespace")
    if len(text) > 180:
        raise SystemExit(f"entry is {len(text)} chars, over the 180 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")


def verify_written(path: str) -> None:
    """Read the file back and demand a byte-exact match with ENTRY."""
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw != ENTRY.encode("utf-8"):
        raise SystemExit(f"read-back mismatch: {path} does not equal ENTRY byte for byte")
    if len(raw) > 180:
        raise SystemExit("written entry is over the 180-byte limit")


def main() -> None:
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    verify_written(path)
    print(f"wrote {len(ENTRY)} chars to {path} (read-back verified)")


if __name__ == "__main__":
    main()
