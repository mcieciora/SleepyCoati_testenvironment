import unittest
from collections import OrderedDict
from app.XmlParser import XmlParser


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_dict = OrderedDict([])
        self.single_elements_types_list = [OrderedDict([('element', ['int'])]), OrderedDict([('element', ['str'])]),
                                           OrderedDict([('element', ['bool'])])]
        self.multi_elements_types_list = [OrderedDict([('element', ['int', 'str'])]),
                                          OrderedDict([('element', ['str', 'bool'])]),
                                          OrderedDict([('element', ['bool', 'int'])])]

    def test_get_usage_patterns_empty_dict(self):
        self.assertEqual(XmlParser.get_usage_patterns(self.empty_dict), []), 'test_get_usage_patterns_empty_dict'

    def test_get_usage_patterns_single_elements_types_list(self):
        expected_results = [[int], [str], [bool]]
        for x in range(len(self.single_elements_types_list)):
            ret_val = XmlParser.get_usage_patterns(self.single_elements_types_list[x])
            self.assertEqual(ret_val, expected_results[x]), 'test_get_usage_patterns_single_elements_types_list'

    def test_get_usage_patterns_multi_elements_types_list(self):
        expected_results = [[int, str], [str, bool], [bool, int]]
        for x in range(len(self.multi_elements_types_list)):
            ret_val = XmlParser.get_usage_patterns(self.multi_elements_types_list[x])
            self.assertEqual(ret_val, expected_results[x]), 'test_get_usage_patterns_multi_elements_types_list'
