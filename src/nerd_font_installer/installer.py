import zipfile
from pathlib import Path

import httpx


def install(url: str, dest: Path) -> bool:
    file_name = _extract_filename(url)
    zip_file_path = dest / file_name
    font_directory = dest / file_name.replace(".zip", "")

    if font_directory.exists():
        return False

    zip_file = httpx.get(url, follow_redirects=True)
    zip_file.raise_for_status()

    with open(zip_file_path, "wb") as f:
        f.write(zip_file.content)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(font_directory)

    return True


def _extract_filename(url: str) -> str:
    return url.split("/")[-1]
