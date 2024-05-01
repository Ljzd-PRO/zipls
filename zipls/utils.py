from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

from zipls.model import ZipLsInfo, FileInfo


def dump_zipls_info(path: Path) -> ZipLsInfo:
    """
    Dump ``ZipLsInfo`` data.
    :param path: Zip file path.
    """
    zipls_info = ZipLsInfo(path=path, size=path.lstat().st_size, files=[])
    zipfile = ZipFile(path)
    for sub_file in zipfile.filelist:
        zipls_info.files.append(
            FileInfo(
                name=sub_file.filename,
                size=sub_file.file_size,
                date=datetime(*sub_file.date_time)
            )
        )
    return zipls_info
