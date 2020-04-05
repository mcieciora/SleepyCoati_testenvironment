import unittest
from app import parser
from os.path import join
from app.Command import Command


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_command = Command('#s', 'set_variable', [str, int])

    def test_get_command_by_structure_empty_string(self):
        self.assertEqual(parser.get_command_by_structure('', join('TestData', 'command.xml')), None), \
            'test_get_command_by_structure_empty_string'

    def test_get_command_by_structure_value_out_of_scope(self):
        self.assertEqual(parser.get_command_by_structure('#a', join('TestData', 'command.xml')), None), \
            'test_get_command_by_structure_value_out_of_scope'

    def test_get_command_by_structure_basic_value(self):
        self.assertEqual(vars(parser.get_command_by_structure('#s', join('TestData', 'command.xml'))),
                         vars(self.basic_command)), 'test_get_command_by_structure_basic_value'
