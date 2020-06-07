import unittest
from app.Parser import Parser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expression_list_str = ['variable_name']
        self.expression_list_int = ['variable_name', 5]
        self.expression_list_bool = ['variable_name', True]

    def test_get_list_elements_type_empty_list(self):
        self.assertEqual(Parser.get_list_elements_type([]), []), 'test_get_list_elements_type_empty_list'

    def test_get_list_elements_type_str_value(self):
        self.assertEqual(Parser.get_list_elements_type(self.expression_list_str), [str]), \
            'test_get_list_elements_type_str_value'

    def test_get_list_elements_type_int_value(self):
        self.assertEqual(Parser.get_list_elements_type(self.expression_list_int), [str, int]), \
            'test_get_list_elements_type_int_value'

    def test_get_list_elements_type_bool_value(self):
        self.assertEqual(Parser.get_list_elements_type(self.expression_list_bool), [str, bool]), \
            'test_get_list_elements_type_bool_value'
