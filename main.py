import os

TEXT = 'When the bank took our truck, my aunt said, "Debt grows in the dark; open every envelope the day it arrives."'


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(TEXT)


if __name__ == "__main__":
    main()
