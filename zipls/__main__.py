import fire
from loguru import logger

from zipls.cli import ZipLsCli


def main():
    try:
        fire.Fire(ZipLsCli)
    except KeyboardInterrupt:
        logger.error("ZipLs was interrupted by the user")


if __name__ == "__main__":
    main()
