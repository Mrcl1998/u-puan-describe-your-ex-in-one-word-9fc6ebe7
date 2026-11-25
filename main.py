#!/usr/bin/env python3
"""Describe Your Ex in One Word — one-word verdict entry.

Writes exactly one word, "Appendix", to entry.txt in the output directory.
Pure standard library, no network, deterministic.

The word: Appendix — the body part surgeons remove when it flares up, and
the pages at the back of a book nobody reads. A vestigial extra: removed,
unread. That is the whole verdict on the ex.
"""

import os
import stat
import sys

WORD = "Appendix"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    # Write exactly the word: no trailing newline, nothing else attached.
    with open(path, "wb") as f:
        f.write(data)
    # Output file readable by the grader's other user; never chmod the
    # output directory itself.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
