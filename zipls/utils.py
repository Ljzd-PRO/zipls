from datetime import datetime
from glob import glob
from pathlib import Path
from typing import Generator, Any
from zipfile import ZipFile, BadZipFile

from rarfile import RarFile

from zipls.model import ZipLsInfo, FileInfo


def dump_zipls_info(path: Path) -> ZipLsInfo:
    """
    Dump ``ZipLsInfo`` data.
    :param path: Zip file path.
    """
    zipls_info = ZipLsInfo(path=path, size=path.lstat().st_size, files=[])
    try:
        zipfile = ZipFile(path)
        for sub_file in zipfile.filelist:
            zipls_info.files.append(
                FileInfo(
                    name=sub_file.filename,
                    size=sub_file.file_size,
                    date=datetime(*sub_file.date_time)
                )
            )
    except BadZipFile:
        rarfile = RarFile(path)
        for sub_file in rarfile:
            zipls_info.files.append(
                FileInfo(
                    name=sub_file.filename,
                    size=sub_file.file_size,
                    date=datetime(*sub_file.date_time)
                )
            )
    return zipls_info


def glob_to_path(*paths: str) -> Generator[Path, Any, None]:
    for path in paths:
        yield from map(Path, glob(path))
