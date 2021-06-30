import argparse
import logging
import sys
import importlib


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


def arg_parser() -> str:
    """
    The function parses cmd arguments. If there are no arguments, it uses the default values.
    :return: tuple of parsed values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('test_module', help='Path to file with tasks')
    args = parser.parse_args()
    return args.test_module


if __name__ == '__main__':
    test_module = arg_parser()
    root_logger = logging.getLogger()
    set_logger(root_logger)
    importlib.import_module(test_module).run_tests()
