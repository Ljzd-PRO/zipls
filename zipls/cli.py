import json

from loguru import logger

from zipls import __version__
from zipls.model import ZipLsInfo, ZipLsDump, settings
from zipls.utils import dump_zipls_info, glob_to_path


class ZipLsCli:
    @classmethod
    def version(cls):
        """ZipLs version"""
        return __version__

    @classmethod
    def schema(cls, path: str = None):
        """Dump JSON Schema of ZipLsInfo"""
        schema_str = json.dumps(ZipLsInfo.model_json_schema(), indent=4)
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(schema_str)
        return schema_str

    @classmethod
    def dump(cls, path: str = None, *zip_files: str):
        """Dump ZipLsInfo data to file"""
        zip_paths = glob_to_path(*zip_files)
        zipls_dump = ZipLsDump()
        for file in zip_paths:
            try:
                zipls_dump.root[file] = dump_zipls_info(file)
            except Exception as e:
                if settings.debug:
                    logger.exception("Error dumping ZipFileInfo")
                else:
                    logger.error(repr(e))
                return None
        zipls_dump_str = zipls_dump.model_dump_json(indent=4)
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(zipls_dump_str)
        return zipls_dump_str

    @classmethod
    def ls(cls, *zip_files: str):
        """Print ZipLsInfo data of zip files"""
        return cls.dump(None, *zip_files)
