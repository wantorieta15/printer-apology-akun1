"""The Printer Apology — Make Fun entry, Akun 1 @walta-exchange (revisi).

One line: a sincere apology from an office printer to its office, written
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only. Gate: UTF-8 text, 1..120 characters, single line.
"""

import os

# Final entry (77 characters). First-person printer voice, concrete scene
# (the printer ate the report), punchline lands on the last words.
# The printer's complaint is explicit: nobody has fed it since 2019.
# Revisi dari teks builder ("...got fed on time", 92 char): keluhan dibuat
# eksplisit + jangkar konkret "since 2019" agar punch langsung tercerna.
# Similarity (SequenceMatcher, autojunk=False) vs pemenang sekeluarga:
# Laugh Sprint R1 0.2844 / R2 0.3246; vs teks Akun 2 0.3111 (berbeda).
# Zero Use R1/R2: teks lengkap juara tidak ditemukan di data prep lokal,
# hanya kutipan terpotong R1 — angka vs Zero Use tidak dihitung dari teks
# utuh yang terverifikasi.
ENTRY = (
    "I'm sorry I ate your report. "
    "It's the first thing anyone's fed me since 2019."
)


def build_entry():
    """Return the entry text, enforcing the bounty gate locally."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 120:
        raise ValueError("entry length %d exceeds 120" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Direct write, no tempfile+rename: the grader reads entry.txt as
    # another uid, so the file must stay world-readable.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
