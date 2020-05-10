from os import getenv
from os.path import join
import unittest
from app import xml_parser
from Command import Command


@unittest.skipIf(getenv('scope') == 'smoke', 'Skipping {}'.format(__file__))
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.one_command_one_element = [Command('#d', 'define_variable', [str])]
        self.one_command_multi_elements = [Command('#s', 'set_variable', [str, int])]
        self.multi_commands_one_element = [Command('#d', 'define_variable', [str]),
                                           Command('#g', 'get_variable', [str])]
        self.multi_commands_multi_elements = [Command('#c', 'test_variable', [str, int]),
                                              Command('#f', 'f_variable', [int, str])]
        self.xmls_path = join(getenv('WORKSPACE'), 'TestCases', 'TestCase_Unittest', 'generate_all_commands_list')

    def test_generate_all_commands_list_one_command_one_element(self):
        ret_val = [vars(x) for x in xml_parser.generate_all_commands_list(join(self.xmls_path,
                                                                               'one_command_one_element.xml'))]
        self.assertEqual(ret_val, [vars(x) for x in self.one_command_one_element]), \
            'test_generate_all_commands_list_one_command_one_element'

    def test_generate_all_commands_list_one_command_multi_elements(self):
        ret_val = [vars(x) for x in xml_parser.generate_all_commands_list(join(self.xmls_path,
                                                                               'one_command_multi_elements.xml'))]
        self.assertEqual(ret_val, [vars(x) for x in self.one_command_multi_elements]), \
            'test_generate_all_commands_list_one_command_multi_elements'

    def test_generate_all_commands_list_multi_commands_one_element(self):
        ret_val = [vars(x) for x in xml_parser.generate_all_commands_list(join(self.xmls_path,
                                                                               'multi_commands_one_element.xml'))]
        self.assertEqual(ret_val, [vars(x) for x in self.multi_commands_one_element]), \
            'test_generate_all_commands_list_one_command_one_element'

    def test_generate_all_commands_list_multi_commands_multi_elements(self):
        ret_val = [vars(x) for x in xml_parser.generate_all_commands_list(join(self.xmls_path,
                                                                          'multi_commands_multi_elements.xml'))]
        self.assertEqual(ret_val, [vars(x) for x in self.multi_commands_multi_elements]), \
            'test_generate_all_commands_list_multi_commands_multi_elements'
