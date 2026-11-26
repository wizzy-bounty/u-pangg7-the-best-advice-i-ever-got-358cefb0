import os
from pathlib import Path

TEXT = "At my brother's funeral, my father whispered, 'Do not rush the empty chair out of the room; love needs somewhere to sit while it learns the new address.'"


def write_entry():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


def main():
    write_entry()


if __name__ == "__main__":
    main()
