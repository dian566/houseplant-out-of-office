#!/usr/bin/env python3
"""Entry for make.fun: The Houseplant Out-of-Office."""

from os import makedirs

ENTRY = (
    "Out of office: not watered since March. The monstera took my window and my will to live. Email her instead."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if len(ENTRY) > 120 or not ENTRY.strip():
        raise ValueError("entry must be a non-empty line of at most 120 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
