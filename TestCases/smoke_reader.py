import unittest
from app import reader
from app.Expression import Expression


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expression_list_basic = ['variable_name', '3']
        self.expression_list_empty_strings = ['', '']
        self.expression_list_empty_list = []
        self.expression_list_ints = [3, 4]
        self.expression_list_bool = ['True', 'False']
        self.expression_list_mix = ['string', 'True', '5']
        self.basic_line = '#d variable_name'
        self.empty_line = '\n'
        self.multi_spaces_line = '   #d   variable_name   '

    def test_value_evaluation_basic_value(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_basic), ['variable_name', 3]), \
            'test_value_evaluation_basic_value'

    def test_value_evaluation_empty_strings(self):
        self.assertEqual(reader.value_evaluation(self.expression_list_empty_strings), []), \
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

    def test_validate_line_basic(self):
        ret_val = reader.validate_line(self.basic_line)
        self.assertEqual(ret_val[0], True), 'test_validate_line_basic step 1'
        self.assertEqual(vars(ret_val[1]), vars(Expression('#d', ['variable_name']))), 'test_validate_line_basic step 2'

    def test_validate_line_empty_line(self):
        ret_val = reader.validate_line(self.empty_line)
        self.assertEqual(ret_val[0], False), 'test_validate_line_empty_line'

    def test_validate_line_multi_spaces_line(self):
        ret_val = reader.validate_line(self.multi_spaces_line)
        self.assertEqual(ret_val[0], True), 'test_validate_line_basic step 1'
        self.assertEqual(vars(ret_val[1]), vars(Expression('#d', ['variable_name']))), 'test_validate_line_basic step 2'
