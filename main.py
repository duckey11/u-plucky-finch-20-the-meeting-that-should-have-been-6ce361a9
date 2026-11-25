#!/usr/bin/env python3
"""Write one one-line joke about a meeting that should have been an email
to /output/entry.txt."""

import os

ENTRY = "We scheduled an hour to discuss the email, then spent it booking another meeting to discuss the email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
