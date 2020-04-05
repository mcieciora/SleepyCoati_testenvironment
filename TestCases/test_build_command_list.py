import unittest
from os.path import join
from app import parser
from app.Expression import Expression


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.example_simple = [Expression('#s', ['variable_name', 5])]
        self.expected_expression_list = [
            Expression('#d', ['variable_name']),
            Expression('#s', ['variable_name', 5]),
            Expression('#s', ['variable_bool', True])
        ]

    def test_build_command_list_simple(self):
        return_value = [vars(x) for x in parser.build_command_list(join('TestData', 'example_simple.co'))]
        self.assertEqual(return_value, [vars(x) for x in self.example_simple]), \
            'test_build_command_list_simple'

    def test_build_command_list_simple_mix(self):
        return_value = [vars(x) for x in parser.build_command_list(join('TestData', 'example_simple_mix.co'))]
        self.assertEqual(return_value, [vars(x) for x in self.expected_expression_list]), \
            'test_build_command_list_simple_mix'

    def test_build_command_list_wrong_command_usage(self):
        return_value = [vars(x) for x in parser.build_command_list(join('TestData', 'example_wrong_command_usage.co'))]
        self.assertEqual(return_value, []), \
            'test_build_command_list_wrong_command_usage'
