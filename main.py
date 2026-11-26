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


if __name__ == "__main__":
    main()
