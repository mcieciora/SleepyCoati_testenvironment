import unittest
from os.path import join
from app import parser
from app.Expression import Expression


class Test(unittest.TestCase):
    def test_check_usage_pattern_correctness_basic_value(self):
        self.assertEqual(parser.check_usage_pattern_correctness(Expression('#d', ['variable']),
                                                                join('TestData', 'command.xml')), True), \
            'test_check_usage_pattern_correctness_basic_value'

    def test_check_usage_pattern_correctness_multi_value(self):
        self.assertEqual(parser.check_usage_pattern_correctness(Expression('#v', ['variable', '2']),
                                                                join('TestData', 'command.xml')), True), \
            'test_check_usage_pattern_correctness_multi_value'

    def test_check_usage_pattern_correctness_structure_value_out_of_scope(self):
        self.assertEqual(parser.check_usage_pattern_correctness(Expression('#a', ['variable']),
                                                                join('TestData', 'command.xml')), False), \
            'test_check_usage_pattern_correctness_structure_value_out_of_scope'

    def test_check_usage_pattern_correctness_negative(self):
        self.assertEqual(parser.check_usage_pattern_correctness(Expression('#d', ['variable', '2']),
                                                                join('TestData', 'command.xml')), False), \
            'test_check_usage_pattern_correctness_negative'
