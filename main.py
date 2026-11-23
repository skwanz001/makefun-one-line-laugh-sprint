#!/usr/bin/env python3
"""One-Line Laugh Sprint: write one original funny line to /output/entry.txt.

Stdlib only. The line is a single original one-liner about everyday life,
at most 200 characters.
"""

import os

LINE = "I meal-prepped on Sunday; by Wednesday, the containers had formed a union and gone on strike."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
