import unittest
from app import reader


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expression_list_basic = ['variable_name', '3']
        self.expression_list_empty_strings = ['', '']
        self.expression_list_empty_list = []
        self.expression_list_ints = [3, 4]
        self.expression_list_bool = ['True', 'False']
        self.expression_list_mix = ['string', 'True', '5']

    def test_value_evaluation_basic_value(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_basic), ['variable_name', 3]), \
            'test_value_evaluation_basic_value'

    def test_value_evaluation_empty_strings(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_empty_strings), ['', '']), \
            'test_value_evaluation_empty_strings'

    def test_value_evaluation_empty_list(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_empty_list), []), \
            'test_value_evaluation_empty_list'

    def test_value_evaluation_ints(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_ints), [3, 4]), 'test_value_evaluation_ints'

    def test_value_evaluation_bools(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_bool), [True, False]), \
            'test_value_evaluation_bools'

    def test_value_evaluation_mix(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_mix), ['string', True, 5]), \
            'test_value_evaluation_mix'
