import unittest
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_usage_pattern_empty_list(self):
        with self.assertRaises(Exception) as context:
            Command('#d', 'define_variable', [])
        self.assertEqual(type(context.exception), TypeError), 'test_usage_pattern_empty_list'

    def test_usage_pattern_basic_types(self):
        int_type = Command('#f', 'find_value', [int])
        self.assertEqual([int], int_type.usage_pattern), 'test_usage_pattern_basic_types int_type'
        bool_type = Command('#f', 'find_value', [bool])
        self.assertEqual([bool], bool_type.usage_pattern), 'test_usage_pattern_basic_types bool_type'
        str_type = Command('#f', 'find_value', [str])
        self.assertEqual([str], str_type.usage_pattern), 'test_usage_pattern_basic_types str_type'

    def test_usage_pattern_mixed_types(self):
        int_str_types = Command('#g', 'get_value', [int, str])
        self.assertEqual([int, str], int_str_types.usage_pattern), 'test_usage_pattern_mixed_types int_str_type'
        bool_int = Command('#g', 'get_value', [bool, int])
        self.assertEqual([int, str], bool_int.usage_pattern), 'test_usage_pattern_mixed_types, bool_int_type'
