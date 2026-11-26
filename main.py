"""Office Joke Open entry: writes one original single-line office joke.

Deterministic, stdlib-only, no network. Writes the exact joke,
byte-identically, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when unset).
"""

import os

JOKE = "I told my boss I thrive under pressure, so now my job title is the office printer."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Runtime validation: re-read what we wrote and assert it is exactly
    # one line, 1-200 characters, byte-identical to the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "entry.txt content mismatch"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"


if __name__ == "__main__":
    main()
