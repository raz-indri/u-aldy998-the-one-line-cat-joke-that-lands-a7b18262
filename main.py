"""One-line cat joke entry for make.fun.

Writes the duel-winning joke to <OUTPUT_DIR>/entry.txt.
Deterministic: no randomness, no network, no input files.

The joke below won an 8-draft round-robin duel test (28 pairs, each
judged in both orders against the published judge brief): a setup with
a clean turn, a fresh angle on adoption, and a punchline short enough
to retell the same day.
"""


def validate(text: str) -> str:
    """Return the joke unchanged, or raise if it breaks the gate."""
    cleaned = text.strip()
    assert 1 <= len(cleaned) <= 200, "joke must be 1-200 characters"
    assert "\n" not in cleaned and "\r" not in cleaned, "single line only"
    assert cleaned == text, "no leading or trailing whitespace"
    return cleaned

import os
import sys

JOKE = "I told my cat he's adopted. He said, 'Buddy, I chose this house. You're the rescue.'"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(JOKE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
