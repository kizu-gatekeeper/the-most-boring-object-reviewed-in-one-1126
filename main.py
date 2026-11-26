"""Entry for make.fun: The Most Boring Object, Reviewed in One Line.

A one-line, one-star review of a doorstop: nine years on the same
door, still upstaged by the wind.
"""
import os

LINE = "One star for the doorstop: it has held the same door, at the same angle, for nine years, and somehow still looks surprised when the wind does its job for it."
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
