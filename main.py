#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry (Account B / past-self-B).

Writes a two-line warning to /output/entry.txt.

Line 1 warns the writer's past self about one specific moment, in a
single sentence. Line 2 says in one sentence why that moment mattered
and what changed because of it.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
280 characters, not only white space.
"""

import os

ENTRY = (
    "Don't delete the voicemail from Dad the night he calls twice — "
    "you will want his voice back more than the storage space.\n"
    "You play it at his funeral, and the nine seconds you almost erased "
    "become the only thing of his you still hear every day."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def verify(text: str) -> None:
    """Enforce the gate limits from RULES.txt."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 280 limit")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        raise ValueError("each line must be non-blank")
    # Each line must be a single sentence (exactly one sentence-ending
    # full stop per line; the em dash in line 1 is punctuation, not a
    # sentence break).
    for i, line in enumerate(lines, 1):
        if line.count(".") != 1 or not line.rstrip().endswith("."):
            raise ValueError(f"line {i} must be exactly one sentence")


def main() -> None:
    verify(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {OUTPUT_PATH}: {len(ENTRY)} chars, "
          f"{len(ENTRY.splitlines())} lines")


if __name__ == "__main__":
    main()
