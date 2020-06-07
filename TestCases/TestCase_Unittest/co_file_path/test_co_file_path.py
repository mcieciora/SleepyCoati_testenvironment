from os import chdir, getenv, path
import unittest
from app.Parser import Parser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.env = getenv('WORKSPACE')
        self.co_file_path_directory = path.join(getenv('WORKSPACE'), 'TestCases', 'TestCase_Unittest', 'co_file_path')

    def test_co_file_path_relative_path(self):
        parser = Parser('example.co', 'empty.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.co_file_path_directory, 'example.co')), \
            'test_co_file_path_relative_path'

    def test_co_file_path_absolute_path(self):
        parser = Parser(path.join(self.co_file_path_directory, 'example.co'), 'empty.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.co_file_path_directory, 'example.co')), \
            'test_co_file_path_absolute_path'

    def test_co_file_path_relative_path_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            Parser('no_directory/example.co', 'empty.xml')
        self.assertEqual(type(context.exception), FileNotFoundError), 'test_co_file_path_relative_path_does_not_exist'

    def test_co_file_path_absolute_path_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            Parser(path.join(self.co_file_path_directory,'example.co'), 'example.co')
        self.assertEqual(type(context.exception), FileNotFoundError), 'test_co_file_path_absolute_path_does_not_exist'

    def test_co_file_path_in_directory(self):
        parser = Parser('directory/example.co', 'empty.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.co_file_path_directory, 'directory', 'example.co')), \
            'test_co_file_path_in_directory'

    def test_co_file_path_double_dot(self):
        chdir('directory')
        parser = Parser('../example.co', 'empty.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.co_file_path_directory, 'example.co')), \
            'test_co_file_path_double_dot'
