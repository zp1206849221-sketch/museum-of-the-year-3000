#!/usr/bin/env python3
"""Museum of the Year 3000 - entry writer.

Writes a single museum label line to /output/entry.txt.
"""
import os

LINE = (
    "Fidget Spinner, c. 2017. Handheld prayer wheel. Anxious citizens spun it "
    "without pause to manufacture calm, a substance their era produced in critically short supply."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
