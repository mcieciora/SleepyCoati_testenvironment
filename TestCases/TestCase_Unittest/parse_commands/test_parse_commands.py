from os import getenv
from os.path import join
import unittest
from app.XmlParser import XmlParser
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.one_command_one_element = [Command('#d', 'define_variable', [str])]
        self.one_command_multi_elements = [Command('#s', 'set_variable', [str, int])]
        self.multi_commands_one_element = [Command('#d', 'define_variable', [str]),
                                           Command('#g', 'get_variable', [str])]
        self.multi_commands_multi_elements = [Command('#c', 'test_variable', [str, int]),
                                              Command('#f', 'f_variable', [int, str])]
        self.xmls_path = join(getenv('WORKSPACE'), 'TestCases', 'TestCase_Unittest', 'parse_commands')

    def test_parse_commands_one_command_one_element(self):
        xml_parser = XmlParser(join(self.xmls_path, 'one_command_one_element.xml'))
        ret_val = [vars(x) for x in xml_parser.parse_commands()]
        self.assertEqual(ret_val, [vars(x) for x in self.one_command_one_element]), \
            'test_parse_commands_one_command_one_element'

    def test_parse_commands_one_command_multi_elements(self):
        xml_parser = XmlParser(join(self.xmls_path, 'one_command_multi_elements.xml'))
        ret_val = [vars(x) for x in xml_parser.parse_commands()]
        self.assertEqual(ret_val, [vars(x) for x in self.one_command_multi_elements]), \
            'test_parse_commands_one_command_multi_elements'

    def test_parse_commands_multi_commands_one_element(self):
        xml_parser = XmlParser(join(self.xmls_path, 'multi_commands_one_element.xml'))
        ret_val = [vars(x) for x in xml_parser.parse_commands()]
        self.assertEqual(ret_val, [vars(x) for x in self.multi_commands_one_element]), \
            'test_parse_commands_multi_commands_one_element'

    def test_parse_commands_multi_commands_multi_elements(self):
        xml_parser = XmlParser(join(self.xmls_path, 'multi_commands_multi_elements.xml'))
        ret_val = [vars(x) for x in xml_parser.parse_commands()]
        self.assertEqual(ret_val, [vars(x) for x in self.multi_commands_multi_elements]), \
            'test_parse_commands_multi_commands_multi_elements'
