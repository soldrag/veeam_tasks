import os
from unittest import TestCase
from task_2.check_hash import parse_line, validate_hash_function, get_file_hash
import string
import hashlib


class TestParseLine(TestCase):

    def setUp(self) -> None:
        self.valid_line = ['main.py', 'sha1', 'b9fe4070b5241ca527199cc594e88ae6287b0cdb']
        self.valid_parse_result = ('main.py', 'sha1', 'b9fe4070b5241ca527199cc594e88ae6287b0cdb')
        self.valid_line_extra_obj = ['main.py', 'sha1', 'b9fe4070b5241ca527199cc594e88ae6287b0cdb', 'some', 'some2']
        self.invalid_parse_result = ('main.py', 'sha1', 'b9fe4070b5241ca527199cc594e88ae6287b0cd1')

    def test_valid_parse_line(self):
        self.assertEqual(parse_line(self.valid_line), self.valid_parse_result)

    def test_valid_parse_extra_obj(self):
        self.assertEqual(parse_line(self.valid_line_extra_obj), self.valid_parse_result)

    def test_invalid_parse_result(self):
        self.assertNotEqual(parse_line(self.valid_line), self.invalid_parse_result)


class TestValidateHashFunction(TestCase):

    def setUp(self) -> None:
        self.valid_hash_name = 'sha1'
        self.invalid_hash_name = 'sha512'

    def test_valid_hash_function(self):
        self.assertTrue(validate_hash_function(self.valid_hash_name))

    def test_invalid_hash_function(self):
        self.assertFalse(validate_hash_function(self.invalid_hash_name))


class TestGetFileHash(TestCase):

    def setUp(self) -> None:
        self.file_for_hash = './tests/test_file_for_hash'
        self.missed_file = './tests/no_file'
        self.valid_hash = '9b4b1c00a843137944fb363e6a0953af022e27e6'
        self.invalid_hash = '9b4b1c00a843137944fb363e6a0953af022e27e1'

    def test_valid_get_hash(self):
        self.assertEqual(get_file_hash(self.file_for_hash, 'sha1'), self.valid_hash)

    def test_invalid_get_hash(self):
        self.assertNotEqual(get_file_hash(self.file_for_hash, 'sha1'), self.invalid_hash)

    def test_missed_file(self):
        self.assertRaises(FileNotFoundError, get_file_hash, self.missed_file, 'sha1')
