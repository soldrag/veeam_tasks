import argparse
import logging
import sys
import test_cases


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
    parser.add_argument('task_file', help='Path to file with tasks')
    parser.add_argument('path_to_files', help='Path to directory with target files')
    args = parser.parse_args()
    return args.task_file, args.path_to_files


if __name__ == '__main__':
    task_file, path_to_files = arg_parser()
    root_logger = logging.getLogger()
    set_logger(root_logger)
    check_hash.main(task_file, path_to_files)