#!/usr/bin/env python3
"""Entry for make.fun bounty 'One Star, Written in Sap'.

Writes a single-line, 1-star review from a houseplant about its human
owner to /output/entry.txt. The line must be 1-279 characters, UTF-8,
one line, with no trailing newline. The output is fully deterministic:
the same text is written on every run.
"""

import os

ENTRY = (
    "One star. He waters me like a rumor, once a month if he remembers, "
    "then acts shocked when I droop. I gave him oxygen, ambiance, and "
    "quiet loyalty. He gave me a chipped pot and a windowsill with no sun."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 279


def validate(text: str) -> None:
    """Ensure the entry is a single valid line within the length gate."""
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"entry length {len(text)} outside {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
