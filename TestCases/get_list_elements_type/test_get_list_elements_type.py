import unittest
from app.Parser import Parser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expression_list_str = ['variable_name']
        self.expression_list_int = ['variable_name', 5]
        self.expression_list_bool = ['variable_name', True]

    def test_get_list_elements_type_empty_list(self):
        self.assertEqual(Parser.get_list_elements_type([]), []), \
            'test_get_list_elements_type_empty_list'

    def test_get_list_elements_type_str_value(self):
        self.assertEqual(Parser(self.expression_list_str, 'command.xml'), [str]), \
            'test_get_list_elements_type_str_value'

    def test_get_list_elements_type_int_value(self):
        self.assertEqual(Parser(self.expression_list_int, 'command.xml'), [int]), \
            'test_get_list_elements_type_int_value'

    def test_get_list_elements_type_bool_value(self):
        self.assertEqual(Parser(self.expression_list_bool, 'command.xml'), [bool]), \
            'test_get_list_elements_type_bool_value'
