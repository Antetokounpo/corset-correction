"""Download all files from the project's Borealis dataset."""

import re
from pathlib import Path
from urllib.parse import unquote

import requests

# Paste the Borealis dataset URL (or DOI) here.
DATASET_URL = "https://demo.borealisdata.ca/dataset.xhtml?persistentId=doi:10.80240/FK2/HLKYWD"

BOREALIS_URL = "https://demo.borealisdata.ca"
OUTPUT_DIR = Path.cwd() / "data" / "raw"


def main() -> None:
    if not DATASET_URL:
        raise SystemExit("Set DATASET_URL in src/corset_correction/download_data.py.")

    # Extract a DOI such as 10.5683/SP3/ABCDEF from a URL or bare DOI.
    match = re.search(r"10\.\d{4,9}/[^\s?#&]+", unquote(DATASET_URL))
    if not match:
        raise SystemExit("The supplied URL does not contain a DOI.")
    persistent_id = f"doi:{match.group(0)}"

    metadata = requests.get(
        f"{BOREALIS_URL}/api/datasets/:persistentId/",
        params={"persistentId": persistent_id},
        timeout=30,
    )
    metadata.raise_for_status()

    files = metadata.json()["data"]["latestVersion"]["files"]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for entry in files:
        data_file = entry["dataFile"]
        filename = entry.get("label") or data_file["filename"]
        destination = OUTPUT_DIR / entry.get("directoryLabel", "") / filename
        destination.parent.mkdir(parents=True, exist_ok=True)

        with requests.get(
            f"{BOREALIS_URL}/api/access/datafile/{data_file['id']}",
            stream=True,
            timeout=60,
        ) as response:
            response.raise_for_status()
            with destination.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    handle.write(chunk)

        print(f"Downloaded {destination}")
