import unittest
from os import getenv
from os.path import join
from app.Parser import Parser
from app.Expression import Expression
from app.Command import Command


@unittest.skipIf(getenv('scope') == 'smoke', 'Skipping {}'.format(__file__))
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = Parser(None, join(getenv('WORKSPACE'), 'TestCases', 'find_pattern_usage', 'TestCase_Unittest',
                                        'command.xml'))
        self.empty_parser = Parser(None, join(getenv('WORKSPACE'), 'TestCases', 'find_pattern_usage',
                                              'TestCase_Unittest', 'empty_command.xml'))
        self.expression_basic = Expression('#d', ['variable_name'])
        self.expression_multi_value = Expression('#s', ['variable', 2])
        self.expression_out_of_scope = Expression('#a', ['variable'])
        self.expression_wrong_usage_pattern = Expression('#d', ['variable', 2])

    def test_find_pattern_usage_basic_value(self):
        pattern_usage = self.parser.find_pattern_usage(self.expression_basic)
        self.assertEqual(pattern_usage[0], True), 'test_find_pattern_usage_basic_value step 1'
        self.assertEqual(vars(pattern_usage[1]), vars(Command('#d', 'define_variable', [str]))), \
            'test_find_pattern_usage_basic_value step 2'

    def test_find_pattern_usage_multi_value(self):
        pattern_usage = self.parser.find_pattern_usage(self.expression_multi_value)
        self.assertEqual(pattern_usage[0], True), 'test_find_pattern_usage_multi_value step 1'
        self.assertEqual(vars(pattern_usage[1]), vars(Command('#s', 'set_variable', [str, int]))), \
            'test_find_pattern_usage_multi_value step 2'

    def test_find_pattern_usage_structure_value_out_of_scope(self):
        self.assertEqual(self.parser.find_pattern_usage(self.expression_out_of_scope), [False]), \
            'test_find_pattern_usage_structure_value_out_of_scope'

    def test_find_pattern_usage_negative(self):
        self.assertEqual(self.parser.find_pattern_usage(self.expression_wrong_usage_pattern), [False]), \
            'test_find_pattern_usage_negative'

    def test_find_pattern_usage_empty_xml(self):
        self.assertEqual(self.empty_parser.find_pattern_usage(self.expression_basic), [False]), \
            'test_find_pattern_usage_structure_value_out_of_scope'
