from datetime import datetime
from glob import glob
from pathlib import Path
from typing import Generator, Any
from zipfile import ZipFile, BadZipFile

from py7zr import SevenZipFile, Bad7zFile
from rarfile import RarFile, NotRarFile

from zipls.exception import UnsupportedFile
from zipls.model import ZipLsInfo, FileInfo


def dump_zipls_info(path: Path) -> ZipLsInfo:
    """
    Dump :class:`ZipLsInfo` data.
    :param path: Zip file path.
    :raise UnsupportedFile
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
        try:
            rarfile = RarFile(path)
            for sub_file in rarfile:
                zipls_info.files.append(
                    FileInfo(
                        name=sub_file.filename,
                        size=sub_file.file_size,
                        date=datetime(*sub_file.date_time)
                    )
                )
        except NotRarFile:
            try:
                seven_zipfile = SevenZipFile(path)
                for sub_file in seven_zipfile.files:
                    zipls_info.files.append(
                        FileInfo(
                            name=sub_file.filename,
                            size=sub_file.uncompressed,
                            date=datetime.fromtimestamp(sub_file.lastwritetime.totimestamp())
                        )
                    )
            except Bad7zFile:
                raise UnsupportedFile(path)
    return zipls_info


def glob_to_path(*paths: str) -> Generator[Path, Any, None]:
    for path in paths:
        yield from map(Path, glob(path))
