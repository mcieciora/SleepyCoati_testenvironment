from os import getenv
from os.path import join
import unittest
from app import reader
from app.Expression import Expression


@unittest.skipIf(getenv('scope') == 'smoke', 'Skipping {}'.format(__file__))
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.expected_expression_list = [
            Expression('#d', ['variable_name']),
            Expression('#s', ['variable_name', 5]),
            Expression('#s', ['variable_bool', True]),
            Expression('#g', ['variable_name']),
            Expression('#g', ['next_variable']),
        ]
        self.cos_path = join(getenv('WORKSPACE'), 'TestCases', 'TestCase_Unittest', 'read_co_file')

    def test_read_co_file_example(self):
        return_value = [vars(x) for x in reader.read_co_file(join(self.cos_path, 'example.co'))]
        self.assertEqual(return_value, [vars(x) for x in self.expected_expression_list]), 'test_read_co_file_example'

    def test_read_co_file_empty(self):
        return_value = [vars(x) for x in reader.read_co_file(join(self.cos_path, 'example_empty.co'))]
        self.assertEqual(return_value, []), 'test_read_co_file_empty'

    def test_read_co_file_empty_lines(self):
        return_value = [vars(x) for x in reader.read_co_file(join(self.cos_path, 'example_empty_lines.co'))]
        self.assertEqual(return_value, [vars(x) for x in self.expected_expression_list]), \
            'test_read_co_file_empty_lines'

    def test_read_co_file_multi_spaces(self):
        return_value = [vars(x) for x in reader.read_co_file(join(self.cos_path, 'example_multi_spaces.co'))]
        self.assertEqual(return_value, [vars(x) for x in self.expected_expression_list]), \
            'test_read_co_file_multi_spaces'
