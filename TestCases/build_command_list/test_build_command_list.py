import unittest
from os import getenv
from app.Parser import Parser
from app.Command import Command
from app.Expression import Expression


@unittest.skipIf(getenv('scope') == 'smoke', 'Skipping {}'.format(__file__))
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = Parser(None, 'command.xml')
        self.read_co_simple = [Expression('#s', ['variable', 5])]
        self.read_co_simple_expected = [Command('#s', 'set_variable', [str, int], ['variable', 5])]
        self.read_co_mix = [
            Expression('#d', ['variable_name']),
            Expression('#s', ['variable', 5])
        ]
        self.read_co_mix_expected = [
            Command('#d', 'define_variable', [str], ['variable_name']),
            Command('#s', 'set_variable', [str, int], ['variable', 5])
        ]
        self.read_co_wrong_usage_pattern = [Expression('#d', ['variable_name', 5])]

    def test_build_command_list_simple(self):
        self.parser.read_co = self.read_co_simple
        return_value = [vars(x) for x in self.parser.build_command_list()]
        self.assertEqual(return_value, [vars(x) for x in self.read_co_simple_expected]), \
            'test_build_command_list_simple'

    def test_build_command_list_simple_mix(self):
        self.parser.read_co = self.read_co_mix
        return_value = [vars(x) for x in self.parser.build_command_list()]
        self.assertEqual(return_value, [vars(x) for x in self.read_co_mix_expected]), \
            'test_build_command_list_simple_mix'

    def test_build_command_list_wrong_command_usage(self):
        self.parser.read_co = self.read_co_wrong_usage_pattern
        return_value = self.parser.build_command_list()
        self.assertEqual(len(return_value), 0), 'test_build_command_list_wrong_command_usage'
