import unittest
from app import reader
from app.Expression import Expression


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_line = '#d variable_name'
        self.empty_line = ''
        self.next_line_separator = '\n'
        self.multi_spaces_line = '   #d   variable_name   '

    def test_validate_line_basic(self):
        ret_val = reader.validate_line(self.basic_line)
        self.assertEqual(ret_val[0], True), 'test_validate_line_basic step 1'
        self.assertEqual(vars(ret_val[1]), vars(Expression('#d', ['variable_name']))), 'test_validate_line_basic step 2'

    def test_validate_line_empty_line(self):
        ret_val = reader.validate_line(self.empty_line)
        self.assertEqual(ret_val[0], False), 'test_validate_line_empty_line'

    def test_validate_line_next_line_separator(self):
        ret_val = reader.validate_line(self.next_line_separator)
        self.assertEqual(ret_val[0], False), 'test_validate_line_next_line_separator'

    def test_validate_line_multi_spaces_line(self):
        ret_val = reader.validate_line(self.multi_spaces_line)
        self.assertEqual(ret_val[0], True), 'test_validate_line_basic step 1'
        self.assertEqual(vars(ret_val[1]), vars(Expression('#d', ['variable_name']))), 'test_validate_line_basic step 2'
