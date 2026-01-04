"""
mirror_images.py

Downloads product images from URLs in a CSV file and saves them locally.
Outputs a new CSV with an added 'LocalImage' column.

Usage: python helpers/mirror_images.py (from project root)
"""

import csv
import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests


# ---------- Config you might change ----------
CSV_FILENAME = "polishes.csv"

# Column names expected in your CSV
NUMBER_COL = "Number"
NAME_COL = "Name"
IMAGE_URL_COL = "Image Address"

# Output settings
IMAGES_DIRNAME = "images"
OUTPUT_CSV_FILENAME = "DND Inventory - with_local_images.csv"

# Download behavior
TIMEOUT_SECONDS = 25
RETRIES = 3
SLEEP_BETWEEN_RETRIES_SECONDS = 1.5
USER_AGENT = "NailPolishInventoryMirror/1.0 (+local script)"


# ---------- Helpers ----------
def sanitize_filename(text: str) -> str:
    """
    Makes a safe filename segment for Windows by removing characters that are not file-friendly.
    """
    text = text.strip()
    # Replace slashes and other "bad" filename characters with underscores
    text = re.sub(r'[<>:"/\\|?*\x00-\x1F]', "_", text)
    # Collapse whitespace/underscores
    text = re.sub(r"[\s_]+", "_", text)
    # Avoid absurdly long filenames
    return text[:120].strip("_")


def infer_extension_from_url(url: str) -> str:
    """
    Attempts to infer a file extension from the URL path.
    Defaults to .jpg if unknown.
    """
    path = urlparse(url).path.lower()
    for ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        if path.endswith(ext):
            return ext
    return ".jpg"


def download_file(url: str, dest_path: Path) -> None:
    """
    Downloads a URL to dest_path with retries and basic error handling.
    """
    headers = {"User-Agent": USER_AGENT}

    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            with requests.get(url, headers=headers, stream=True, timeout=TIMEOUT_SECONDS) as r:
                r.raise_for_status()

                # Ensure destination folder exists
                dest_path.parent.mkdir(parents=True, exist_ok=True)

                # Write to disk in chunks (safer for large files)
                with open(dest_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 128):
                        if chunk:
                            f.write(chunk)

            return  # success
        except Exception as e:
            last_err = e
            if attempt < RETRIES:
                time.sleep(SLEEP_BETWEEN_RETRIES_SECONDS)

    # If we got here, all retries failed
    raise RuntimeError(f"Failed to download {url} after {RETRIES} attempts: {last_err}")


def main() -> None:
    """
    Main runner:
    - Loads rows from CSV
    - Downloads each image
    - Writes updated CSV with LocalImage paths
    """
    # Support running from either project root or helpers/ folder
    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / CSV_FILENAME
    images_dir = base_dir / IMAGES_DIRNAME
    output_csv_path = base_dir / OUTPUT_CSV_FILENAME

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")

    # Read CSV
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    # Add output column if missing
    if "LocalImage" not in fieldnames:
        fieldnames.append("LocalImage")

    # Download each image
    success = 0
    skipped = 0
    failed = 0

    for i, row in enumerate(rows, start=1):
        number = str(row.get(NUMBER_COL, "")).strip()
        name = str(row.get(NAME_COL, "")).strip()
        img_url = str(row.get(IMAGE_URL_COL, "")).strip()

        # If there's no URL, we can't download anything
        if not img_url:
            row["LocalImage"] = ""
            skipped += 1
            continue

        # Build a stable filename using number + name
        safe_num = sanitize_filename(number) if number else f"row{i}"
        safe_name = sanitize_filename(name) if name else "unknown"
        ext = infer_extension_from_url(img_url)

        filename = f"{safe_num}-{safe_name}{ext}"
        dest_path = images_dir / filename

        # If already downloaded, don’t re-download
        if dest_path.exists() and dest_path.stat().st_size > 0:
            row["LocalImage"] = str(Path(IMAGES_DIRNAME) / filename).replace("\\", "/")
            skipped += 1
            continue

        try:
            download_file(img_url, dest_path)
            row["LocalImage"] = str(Path(IMAGES_DIRNAME) / filename).replace("\\", "/")
            success += 1
            print(f"[{i}/{len(rows)}] Downloaded: {filename}")
        except Exception as e:
            failed += 1
            row["LocalImage"] = ""
            print(f"[{i}/{len(rows)}] FAILED: {number} {name} -> {e}")

    # Write updated CSV
    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print("\nDone.")
    print(f"Saved images to: {images_dir}")
    print(f"Wrote updated CSV: {output_csv_path}")
    print(f"Downloaded: {success}, Skipped: {skipped}, Failed: {failed}")


if __name__ == "__main__":
    main()
