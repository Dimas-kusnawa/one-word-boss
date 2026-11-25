"""One Word for the Boss (make.fun).

Writes a single word describing the boss to /output/entry.txt.
The word: credittaker — the boss who takes credit for your work.
"""

import os

WORD = "credittaker"
# One word, 11 characters, inside the 1-30 gate. No spaces, no caption.
# Why this word: every workplace has one — the boss who presents your
# work as theirs in the meeting. A colleague repeats it at lunch because
# it lands on its own, and it travels: kitchen, warehouse or office.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # Exactly the word, no trailing newline: the gate counts characters.
        f.write(WORD)


if __name__ == "__main__":
    main()
