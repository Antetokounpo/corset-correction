"""Copy the raw dataset to the processed data directory."""

import shutil
from pathlib import Path

RAW_DIR = Path("data") / "raw"
PROCESSED_DIR = Path("data") / "processed"


def main() -> None:
    shutil.copytree(RAW_DIR, PROCESSED_DIR, dirs_exist_ok=True)
    print("Data preprocessed")


if __name__ == "__main__":
    main()
