import unittest
from os.path import join
from app import parser
from app.Expression import Expression
from app.Command import Command


class Test(unittest.TestCase):
    def test_find_pattern_usage_basic_value(self):
        pattern_usage = parser.find_pattern_usage(Expression('#d', ['variable']), join('TestData', 'command.xml'))
        self.assertEqual(pattern_usage[0], True), 'test_find_pattern_usage_basic_value step 1'
        self.assertEqual(vars(pattern_usage[1]), vars(Command('#d', 'define_variable', [str]))), \
            'test_find_pattern_usage_basic_value step 2'

    def test_find_pattern_usage_multi_value(self):
        pattern_usage = parser.find_pattern_usage(Expression('#s', ['variable', 2]), join('TestData', 'command.xml'))
        self.assertEqual(pattern_usage[0], True), 'test_find_pattern_usage_multi_value step 1'
        self.assertEqual(vars(pattern_usage[1]), vars(Command('#s', 'set_variable', [str, int]))), \
            'test_find_pattern_usage_multi_value step 2'

    def test_find_pattern_usage_structure_value_out_of_scope(self):
        self.assertEqual(parser.find_pattern_usage(Expression('#a', ['variable']),
                                                                join('TestData', 'command.xml')), [False]), \
            'test_find_pattern_usage_structure_value_out_of_scope'

    def test_find_pattern_usage_negative(self):
        self.assertEqual(parser.find_pattern_usage(Expression('#d', ['variable', 2]),
                                                                join('TestData', 'command.xml')), [False]), \
            'test_find_pattern_usage_negative'
