import unittest
from app import Parser
from os import getenv
from os.path import join
from app.Parser import Parser
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_parser = Parser(None, join(getenv('WORKSPACE'), 'TestCases', 'get_command_by_structure',
                                              'empty_command.xml'))
        self.parser_basic = Parser(None, join(getenv('WORKSPACE'), 'TestCases', 'get_command_by_structure',
                                              'command.xml'))
        self.parser_multiset = Parser(None, join(getenv('WORKSPACE'), 'TestCases', 'get_command_by_structure',
                                                 'command_multi_set.xml'))
        self.basic_command = [Command('#s', 'set_variable', [str, int])]
        self.multi_set = [
            Command('#s', 'set_variable', [str, int]),
            Command('#s', 'set_variable', [str, bool]),
            Command('#s', 'set_variable', [str, str]),
        ]

    def test_get_command_by_structure_empty_string(self):
        self.assertEqual(self.parser_basic.get_command_by_structure(''), []), \
            'test_get_command_by_structure_empty_string'

    def test_get_command_by_structure_value_out_of_scope(self):
        self.assertEqual(self.parser_basic.get_command_by_structure('#a'), []), \
            'test_get_command_by_structure_value_out_of_scope'

    def test_get_command_by_structure_basic_value(self):
        parser_command = [vars(x) for x in self.parser_basic.get_command_by_structure('#s')]
        self.assertEqual(parser_command, [vars(x) for x in self.basic_command]), \
            'test_get_command_by_structure_basic_value'

    def test_get_command_by_structure_multi_set(self):
        parser_command = [vars(x) for x in self.parser_multiset.get_command_by_structure('#s')]
        self.assertEqual(parser_command, [vars(x) for x in self.multi_set]), \
            'test_get_command_by_structure_basic_value'

    def test_get_command_by_structure_empty_xml_file(self):
        self.assertEqual(self.empty_parser.get_command_by_structure('#s'), []), \
            'test_get_command_by_structure_empty_xml_file'
