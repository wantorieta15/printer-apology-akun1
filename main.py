"""The Printer Apology — Make Fun entry (program/v1, python3.13, stdlib only).

Writes one line, an apology note from an office printer to its office,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Gate: UTF-8 text, 1 to 120 characters, not only whitespace.
"""

import os

# Final entry (92 characters). First-person printer voice, concrete scene
# (ate the report), punchline lands on the last words.
ENTRY = (
    "I'm sorry I ate your report. "
    "It was the only thing in this office that ever got fed on time."
)


def build_entry():
    """Return the entry text, enforcing the 120-character gate locally."""
    text = ENTRY.strip()
    if not (1 <= len(text) <= 120):
        raise ValueError("entry length %d outside 1..120" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Direct write (no atomic tempfile+replace): the grader reads this
    # file as another uid, so it must stay world-readable.
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
