import argparse
import logging
import sys


def set_logger(logger) -> None:
    """
    Set logger for project
    """
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(f'%(levelname)s - %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def arg_parser() -> tuple:
    """
    The function parses cmd arguments. If there are no arguments, it uses the default values.
    :return: tuple of parsed values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('xml_file')
    args = parser.parse_args()
    return pass


if __name__ == '__main__':
    root_logger = logging.getLogger()
    set_logger(root_logger)
    file_copy.main(xml_file=xms_file, error_ignore=error_ignore, folder_create=folder_create, file_replace=file_replace)
