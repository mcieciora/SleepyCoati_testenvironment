from os import chdir, getenv, path
import unittest
from app.Parser import Parser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.xml_file_path_directory = path.join(getenv('WORKSPACE'), 'TestCases', 'TestCase_Unittest', 'xml_file_path')

    def test_xml_file_path_relative_path(self):
        parser = Parser('empty.co', 'commands.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.xml_file_path_directory, 'commands.xml')), \
            'test_xml_file_path_relative_path'

    def test_xml_file_path_absolute_path(self):
        parser = Parser('empty.co', path.join(self.xml_file_path_directory, 'commands.xml'))
        self.assertEqual(parser.xml_file_path, path.join(self.xml_file_path_directory, 'commands.xml')), \
            'test_xml_file_path_absolute_path'

    def test_xml_file_path_relative_path_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            Parser('empty.co', 'no_directory/commands.xml')
        self.assertEqual(type(context.exception), FileNotFoundError), 'test_xml_file_path_relative_path_does_not_exist'

    def test_xml_file_path_absolute_path_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            Parser('empty.co', path.join(self.xml_file_path_directory, 'no_directory/commands.xml'))
        self.assertEqual(type(context.exception), FileNotFoundError), 'test_xml_file_path_absolute_path_does_not_exist'

    def test_xml_file_path_in_directory(self):
        parser = Parser('empty.co', 'directory/commands.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.xml_file_path_directory, 'directory', 'empty.xml')), \
            'test_xml_file_path_in_directory'

    def test_xml_file_path_double_dot(self):
        chdir('directory')
        parser = Parser('empty.co', '../commands.xml')
        self.assertEqual(parser.xml_file_path, path.join(self.xml_file_path_directory, 'commands.xml')), \
            'test_xml_file_path_double_dot'
