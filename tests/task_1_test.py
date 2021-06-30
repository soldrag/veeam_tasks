import os
from unittest import TestCase
from task_1.file_copy import parse_xml, check_exists_file, checking_for_create_folder
from xml.etree.ElementTree import ParseError


class TestXMLParsing(TestCase):

    def setUp(self) -> None:
        self.xml_config = './tests/test_xml.xml'
        self.broken_xml_config = './tests/test_broken_xml.xml'
        self.missing_xml_config = './tests/some_xml.xml'
        self.valid_result = [
            ("C:\\Windows\\system32", "C:\\Program files", "kernel32.dll"),
            ("/var/log", "/etc", "server.log"),
        ]
        self.invalid_result = [
            ("C:\\Windows\\system31", "C:\\Program files", "kernel32.dll"),
            ("/var/log", "/etc", "server.log"),
        ]

    def test_valid_parse_xml(self):
        self.assertEqual(parse_xml(self.xml_config), self.valid_result)

    def test_not_valid_parse_xlm(self):
        self.assertNotEqual(parse_xml(self.xml_config), self.invalid_result)

    def test_parse_invalid_xml(self):
        self.assertRaises(ParseError, parse_xml, self.broken_xml_config)

    def test_parse_missing_xml(self):
        self.assertRaises(FileNotFoundError, parse_xml, self.missing_xml_config)

    def test_invalid_argument(self):
        self.assertRaises(TypeError, parse_xml, None)


class TestCheckExistsFile(TestCase):
    def setUp(self) -> None:
        with open('./tests/test_exists', 'w')as f:
            f.write('1')
        self.path = './tests'
        self.file_name = 'test_exists'
        self.false_file_name = 'test_not_exists'

    def test_file_exists(self):
        self.assertIsNone(check_exists_file(self.path, self.file_name))

    def test_file_not_exists(self):
        self.assertRaises(FileNotFoundError, check_exists_file, self.path, self.false_file_name)

    def test_invalid_argument(self):
        self.assertRaises(TypeError, check_exists_file, None, None)

    def tearDown(self) -> None:
        os.remove('./tests/test_exists')


class TestCheckingCreateFolder(TestCase):

    def setUp(self) -> None:
        self.real_destination = './tests'
        self.fake_destination = './tests/1'

    def test_folder_exists(self):
        self.assertIsNone(checking_for_create_folder(self.real_destination, True))

    def test_folder_not_exists_not_create(self):
        self.assertRaises(FileNotFoundError, checking_for_create_folder, self.fake_destination, False)

    def test_invalid_arguments(self):
        self.assertRaises(TypeError, checking_for_create_folder, None, None)
