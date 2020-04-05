import unittest
from app import parser
from os.path import join
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_command = [Command('#s', 'set_variable', [str, int])]
        self.multi_set = [Command('#s', 'set_variable', [str, int]), Command('#s', 'set_variable', [str, bool])]

    def test_get_command_by_structure_empty_string(self):
        self.assertEqual(parser.get_command_by_structure('', join('TestData', 'command.xml')), []), \
            'test_get_command_by_structure_empty_string'

    def test_get_command_by_structure_value_out_of_scope(self):
        self.assertEqual(parser.get_command_by_structure('#a', join('TestData', 'command.xml')), []), \
            'test_get_command_by_structure_value_out_of_scope'

    def test_get_command_by_structure_basic_value(self):
        parser_command = [vars(x) for x in parser.get_command_by_structure('#s', join('TestData', 'command.xml'))]
        self.assertEqual(parser_command, [vars(x) for x in self.basic_command]), \
            'test_get_command_by_structure_basic_value'

    def test_get_command_by_structure_multi_set(self):
        parser_command = [vars(x) for x in parser.get_command_by_structure('#s',
                                                                           join('TestData', 'command_multi_set.xml'))]
        self.assertEqual(parser_command, [vars(x) for x in self.multi_set]), \
            'test_get_command_by_structure_basic_value'
