import file_copy
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
    parser.add_argument('-f', '--force', action='store_true', help='Replace file flag')
    parser.add_argument('-i', '--ignore', action='store_true', help='Ignore errors flag')
    parser.add_argument('-c', '--create', action='store_true', help='Create dst folder')
    args = parser.parse_args()
    return args.xml_file, args.ignore, args.create, args.force


if __name__ == '__main__':
    xms_file, error_ignore, folder_create, file_replace = arg_parser()
    root_logger = logging.getLogger()
    set_logger(root_logger)
    file_copy.main(xml_file=xms_file, error_ignore=error_ignore, folder_create=folder_create, file_replace=file_replace)
