import os

ENTRY = "After my first failed exam, my mother said, \"Shame is a bad teacher; bring me the questions you missed.\""


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(output_dir)


if __name__ == "__main__":
    main()
