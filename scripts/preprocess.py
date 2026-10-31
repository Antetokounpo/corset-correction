from pathlib import Path
import shutil

RAW_DIR = Path("data") / "raw"
PROCESSED_DIR = Path("data") / "processed"

shutil.copytree(RAW_DIR, PROCESSED_DIR, dirs_exist_ok=True)

print("Data preprocessed")
