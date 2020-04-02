import unittest

from app import Command
from app import reader


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expression_list_basic = ['variable_name', '3']
        self.expression_list_empty_strings = ['', '']
        self.expression_list_empty_list = []
        self.expression_list_ints = [3, 4]
        self.expression_list_bool_value = ['variable_name', True]
        self.command_list = [Command.Command('#d', 'define_variable',  [str]),
                             Command.Command('#v', 'variable_define_set', [str, int])]

    def test_get_list_elements_type_basic_value(self):
        self.assertEqual(reader.get_list_elements_type(self.expression_list_basic), [str, int]), \
            'test_get_list_elements_type_basic_value'

    def test_expression_list_empty_strings(self):
        self.assertEqual(reader.get_list_elements_type(self.expression_list_empty_strings), [str, str]), \
            'test_expression_list_empty_strings'

    def test_expression_list_empty_list(self):
        self.assertEqual(reader.get_list_elements_type(self.expression_list_empty_list), []), \
            'test_expression_list_empty_list'

    def test_expression_list_ints(self):
        self.assertEqual(reader.get_list_elements_type(self.expression_list_ints), [int, int]), \
            'test_expression_list_ints'

    def test_expression_list_bool_value(self):
        self.assertEqual(reader.get_list_elements_type(self.expression_list_bool_value), [str, str]), \
            'test_expression_list_bool_value'

    def test_check_usage_pattern_correctness_basic_value(self):
        self.assertEqual(reader.check_usage_pattern_correctness('#d', ['variable']), True), \
            'test_check_usage_pattern_correctness_basic_value'

    def test_check_usage_pattern_correctness_multi_value(self):
        self.assertEqual(reader.check_usage_pattern_correctness('#v', ['variable', '2']), True), \
            'test_check_usage_pattern_correctness_multi_value'

    def test_check_usage_pattern_correctness_structure_value_out_of_scope(self):
        self.assertEqual(reader.check_usage_pattern_correctness('#a', ['variable']), False), \
            'test_check_usage_pattern_correctness_structure_value_out_of_scope'

    def test_check_usage_pattern_correctness_negative(self):
        self.assertEqual(reader.check_usage_pattern_correctness('#d', ['variable', '2']), False), \
            'test_check_usage_pattern_correctness_negative'
