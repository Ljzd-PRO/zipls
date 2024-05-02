from pathlib import Path


class UnsupportedFile(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Unsupported file: {path}, only zip, rar, 7z files are accessible")
