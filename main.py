"""One-Line Office Jokes — make.fun entry program.

Writes a single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, one line, 1-199 characters).

Python standard library only.
"""

import os

ENTRY = (
    "The printer only jams at 4:59 on a Friday, "
    "right after I hit print on the thing due at 5."
)


def main():
    # Fail loudly instead of writing an entry the gate would refuse:
    # one line, 1-199 characters, not only whitespace, no trailing newline.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert ENTRY.strip() != "", "entry must not be only whitespace"
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
