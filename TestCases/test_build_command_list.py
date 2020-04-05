import unittest
from os.path import join
from app import parser
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.example_simple = [Command('#s', 'set_variable', [str, int], ['variable_name', 5])]
        self.expected_expression_list = [
            Command('#d', 'define_variable', [str], ['variable_name']),
            Command('#s', 'set_variable', [str, int], ['variable_name', 5])
            ]

    def test_build_command_list_simple(self):
        return_value = [vars(x) for x in parser.build_command_list(join('TestData', 'example_simple.co'),
                                                                   join('TestData', 'command.xml'))]
        self.assertEqual(return_value, [vars(x) for x in self.example_simple]), \
            'test_build_command_list_simple'

    def test_build_command_list_simple_mix(self):
        return_value = [vars(x) for x in parser.build_command_list(join('TestData', 'example_simple_mix.co'),
                                                                   join('TestData', 'command.xml'))]
        self.assertEqual(return_value, [vars(x) for x in self.expected_expression_list]), \
            'test_build_command_list_simple_mix'

    def test_build_command_list_wrong_command_usage(self):
        return_value = parser.build_command_list(join('TestData', 'example_wrong_command_usage.co'),
                                                 join('TestData', 'command.xml'))
        self.assertEqual(len(return_value), 0), 'test_build_command_list_wrong_command_usage'
