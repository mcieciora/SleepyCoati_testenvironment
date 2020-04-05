import unittest
from app import parser


class Test(unittest.TestCase):
    def test_get_list_elements_type_str_value(self):
        self.assertEqual(parser.get_list_elements_type(['variable_name']), [str]), \
            'test_get_list_elements_type_str_value'

    def test_get_list_elements_type_int_value(self):
        self.assertEqual(parser.get_list_elements_type([5]), [int]), \
            'test_get_list_elements_type_int_value'

    def test_get_list_elements_type_bool_value(self):
        self.assertEqual(parser.get_list_elements_type([True]), [bool]), \
            'test_get_list_elements_type_bool_value'

    def test_get_list_elements_type_empty_list(self):
        self.assertEqual(parser.get_list_elements_type([]), []), \
            'test_get_list_elements_type_empty_list'

    def test_get_list_elements_type_list_ints(self):
        self.assertEqual(parser.get_list_elements_type(['string_value', True, 5]), [str, bool, int]), \
            'test_get_list_elements_type_list_ints'
