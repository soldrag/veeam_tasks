import hashlib
from os.path import isfile, join
import string
from typing import Tuple
import logging

logger = logging.getLogger()


def parse_line(arguments_line: list) -> Tuple[str, ...]:
    """Parsing line in config file"""
    file_name, hash_function, hash_result, *_ = arguments_line
    return file_name, hash_function.lower(), hash_result


def validate_file(file_path: str) -> bool:
    return isfile(file_path)


def validate_hash_function(hash_function: str) -> object:
    list_supported_hashes = ['md5', 'sha1', 'sha256']
    return hash_function in list_supported_hashes


def validate_hash_result(hash_result: str, hash_function: str) -> bool:
    """Validating hash from tasks file."""
    is_hex = all(digit in string.hexdigits for digit in hash_result)
    len_validator = {
        'md5': 32,
        'sha1': 40,
        'sha256': 64
    }
    is_len_hash = len(hash_result) == len_validator[hash_function]
    return is_hex and is_len_hash


def get_file_hash(file_path: str, hash_function) -> str:
    """Getting file hash. Uses 1Kb chunks"""
    hash_functions = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
    }
    file_hash = hash_functions.get(hash_function)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(1024):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def main(task_file: str, path: str) -> None:
    """The main function call all other functions and manages the process."""
    with open(task_file, 'r') as f:
        while line := f.readline().split():
            if len(line) < 3:
                continue
            file_name, hash_function, hash_result = parse_line(line)
            file_path = join(path, file_name)
            if not validate_file(file_path):
                print(f'{file_name} NOT FOUND')
                continue
            if not validate_hash_function(hash_function):
                print(f'{file_name} FAIL')
                continue
            if not validate_hash_result(hash_result, hash_function):
                print(f'{file_name} FAIL')
                continue
            file_hash = get_file_hash(file_path, hash_function)
            if file_hash == hash_result:
                print(f'{file_name} OK')
            else:
                print(f'{file_name} FAIL')
