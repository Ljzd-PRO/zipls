from datetime import datetime
from pathlib import Path
from typing import List, Dict

from pydantic import BaseModel, RootModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class FileInfo(BaseModel):
    """
    Information of a file
    :ivar name: Relative path of the file.
    :ivar size: Size of the file (Byte).
    :ivar date: The date of the file.
    """
    name: str
    size: int
    date: datetime


class ZipLsInfo(BaseModel):
    """
    Information of a zip file
    :ivar path: Path of the zip file.
    :ivar size: Size of the zip file.
    :ivar files: Files in the zip file.
    """
    path: Path
    size: int
    files: List[FileInfo] = []


class ZipLsDump(RootModel):
    """
    Result data of ZipLs
    """
    root: Dict[Path, ZipLsInfo] = {}


class Settings(BaseSettings):
    debug: bool = False

    model_config = SettingsConfigDict(env_prefix="zipls_")


settings = Settings()
