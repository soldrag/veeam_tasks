import xml.etree.ElementTree as ET
from typing import List, Tuple
from os.path import isdir, isfile, join
import os
import shutil
import logging

logger = logging.getLogger()


def parse_xml(xml_file: str) -> List[Tuple[str, ...]]:
    """
    The function parses xml config file.
    :param xml_file: path to xml file
    :return: list of tuples with params
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return [(item.get('source_path'), item.get('destination_path'), item.get('file_name')) for item in root]


def check_exists_file(source_path: str, file_name: str) -> None:
    """
    Checking if file exists.
    """
    if not isfile(join(source_path, file_name)):
        raise FileNotFoundError(f'File "{file_name}" not found.')


def checking_for_create_folder(destination_path: str, create_folder_flag: bool) -> None:
    """
    Checking if path exists.
    """
    if not isdir(destination_path):
        if create_folder_flag:
            os.mkdir(destination_path)
        else:
            raise FileNotFoundError(f'Directory "{destination_path}" not found.')


def checking_for_replace(destination_path: str, file_name: str, file_replace_flag: bool) -> bool:
    """
    Checking if need replace existed file. Displays a dialog to confirm if the flag for overwrite is not set.
    """
    if file_replace_flag or not isfile(join(destination_path, file_name)):
        flag = True
    else:
        logger.warning(f'File "{join(destination_path, file_name)}" already exist.')
        flag = input(f'You wanna replace "{join(destination_path, file_name)}" (y, n)? ').lower() == 'y'
    return flag


def copy_file(source_path: str, destination_path: str, file_name: str) -> None:
    """Copy file to destination folder"""
    shutil.copy(join(source_path, file_name), destination_path)


def main(xml_file: str, error_ignore: bool = True, folder_create: bool = False, file_replace: bool = False):
    """The main function call all other functions and manages the process."""
    copy_items = parse_xml(xml_file)
    for item in copy_items:
        source_path, destination_path, file_name = item
        try:
            check_exists_file(source_path, file_name)
            checking_for_create_folder(destination_path, folder_create)
            if not checking_for_replace(destination_path, file_name, file_replace):
                continue
            copy_file(source_path, destination_path, file_name)
            logger.info(f'File "{file_name}" successfully copied to "{destination_path}" ')
        except (FileNotFoundError, PermissionError) as err:
            if error_ignore:
                logger.error(err)
                continue
            else:
                raise err
