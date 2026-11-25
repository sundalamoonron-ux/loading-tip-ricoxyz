#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (max 200 chars, one line) to /output/entry.txt.

The tip is the winner of an internal pairwise tournament over 10 variants,
scored against the judge's five criteria: (1) a real loading-screen tip for
stressed developers and AI coding agents, (2) a real laugh via a turn or
punchline, (3) lands in a glance, (4) speaks to the dev and the agent at
once, (5) fresh, not a coffee/deadline/compile rerun.
"""

import os

TIP = (
    "Loading tip: the agent finished the feature. The tests failed. "
    "You both learned something. Only one of you will remember it."
)


def validate_tip(tip: str) -> None:
    """Gate: the entry must be UTF-8 text of 1-200 chars, one line, not blank.

    Mirrors the sealed gate scorer: /output/entry.txt must hold 1 to 200
    characters, not only white space, and a single line. Raises ValueError
    on any violation so a bad tip never reaches the file.
    """
    if not isinstance(tip, str):
        raise ValueError("tip must be a string")
    if not tip.strip():
        raise ValueError("tip must not be blank or only whitespace")
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    if not 1 <= len(tip) <= 200:
        raise ValueError(f"tip must be 1-200 characters, got {len(tip)}")
    tip.encode("utf-8")  # must be encodable as UTF-8


def main() -> None:
    validate_tip(TIP)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
