#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — entry program.

Writes one line to /output/entry.txt: an office joke about the office
printer announcing its retirement and giving HR two solid weeks of
paper jams as its notice. One line of UTF-8 text inside the gate of
1 to 200 characters, written with no trailing newline.
"""

import os
from pathlib import Path

JOKE = (
    "Our office printer announced its retirement today. HR asked for "
    "two weeks' notice, so it gave them two solid weeks of paper jams."
)

OUTPUT_NAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    # write_text adds nothing of its own: the file ends with the
    # joke's final period, keeping the count at exactly 129.
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
