import unittest

from app import Command
from app import reader


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.command_list = [Command.Command('#d', 'define_variable',  [str]),
                             Command.Command('#v', 'variable_define_set', [str, int]),
                             Command.Command('#s', 'set_variable',  [str, int]),
                             Command.Command('#g', 'get_variable', [str])]
        reader.command_list = self.command_list
        self.expression_list_basic = ['variable_name', '3']
        self.expression_list_empty_strings = ['', '']
        self.expression_list_empty_list = []
        self.expression_list_ints = [3, 4]

    def test_get_command_by_structure_empty_string(self):
        self.assertEqual(reader.get_command_by_structure(''), None), 'test_get_command_by_structure_empty_string'

    def test_get_command_by_structure_value_out_of_scope(self):
        self.assertEqual(reader.get_command_by_structure('#a'), None), \
            'test_get_command_by_structure_value_out_of_scope'

    def test_get_command_by_structure_basic_value(self):
        self.assertEqual(reader.get_command_by_structure('#v'), self.command_list[1]), \
            'test_get_command_by_structure_basic_value'

    def test_convert_ints_basic_value(self):
        self.assertEqual(reader.convert_ints(self.expression_list_basic), ['variable_name', 3]), \
            'test_convert_ints_basic_value'

    def test_expression_list_empty_strings(self):
        self.assertEqual(reader.convert_ints(self.expression_list_empty_strings), ['', '']), \
            'test_expression_list_empty_strings'

    def test_expression_list_empty_list(self):
        self.assertEqual(reader.convert_ints(self.expression_list_empty_list), []), 'test_expression_list_empty_list'

    def test_expression_list_ints(self):
        self.assertEqual(reader.convert_ints(self.expression_list_ints), [3, 4]), 'test_expression_list_ints'
