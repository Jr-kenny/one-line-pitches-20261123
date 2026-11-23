#!/usr/bin/env python3
"""Entry program for make.fun u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes the one-sentence pitch to /output/entry.txt. Python 3, stdlib only.
"""
import os

PITCH = "You have carried that app idea around for years, so just describe it in plain words to an AI agent on make.fun and watch it turn into a working first version today, no coding needed."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(PITCH) <= 240:
        raise SystemExit("pitch must be 1 to 240 characters")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read back what was written: the entry must be exactly the pitch,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != PITCH:
        raise SystemExit("entry.txt does not match the pitch")


if __name__ == "__main__":
    main()
