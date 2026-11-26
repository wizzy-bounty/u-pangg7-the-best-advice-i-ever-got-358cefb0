import os
from pathlib import Path

ADVICE = "When my father kept pushing my hand away at the clinic, the nurse said, \"Offer him the chair before you offer your arm.\""


def output_directory():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    output_dir = output_directory()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ADVICE, encoding="utf-8")


if __name__ == "__main__":
    main()
