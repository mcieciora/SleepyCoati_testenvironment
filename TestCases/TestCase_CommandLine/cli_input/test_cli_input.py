import unittest
from os import environ
from subprocess import check_output
from app import main
from os.path import abspath


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.main_path = abspath(main.__file__)
        self.help_option = 'SleepyCoati.py [OPTION]... [FILE]...\nAvailable options:\n\t-h, --help	Show help guide' \
                           '\n\t-v, --verbose	Change verbosity, [LOW|MEDIUM|HIGH]\n\t-i, --input	Declare input ' \
                           'package for compilation\n'
        self.python_version = environ['python_version']

    def test_main_py_call(self):
        ret_val = check_output([self.python_version, self.main_path]).decode(encoding='UTF-8')
        self.assertEqual(ret_val, self.help_option)

    def test_main_py_call_with_help_option(self):
        ret_val_1 = check_output([self.python_version, self.main_path, '--help']).decode(encoding='UTF-8')
        self.assertEqual(ret_val_1, self.help_option)
        ret_val_2 = check_output([self.python_version, self.main_path, '-h']).decode(encoding='UTF-8')
        self.assertEqual(ret_val_2, self.help_option)
