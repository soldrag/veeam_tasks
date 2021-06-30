from unittest import TestCase
from file_copy import parse_xml
from xml.etree.ElementTree import ParseError


class TestXMLParsing(TestCase):

    def setUp(self) -> None:
        self.text_xml1 = 'test_xml.xml'
        self.text_broken_xml = 'test_broken_xml.xml'
        self.positive_result1 = [
            ("C:\\Windows\\system32", "C:\\Program files", "kernel32.dll"),
            ("/var/log", "/etc", "server.log"),
        ]
        self.negative_result1 = [
            ("C:\\Windows\\system31", "C:\\Program files", "kernel32.dll"),
            ("/var/log", "/etc", "server.log"),
        ]

    def test_positive_parse_xml(self):
        self.assertEqual(parse_xml(self.text_xml1), self.positive_result1)

    def test_negative_parse_xlm(self):
        self.assertNotEqual(parse_xml(self.text_xml1), self.negative_result1)

    def test_invalid_parse_xml(self):
        self.assertRaises(ParseError, parse_xml, self.text_broken_xml)
