from os import getcwd, listdir
from os.path import join
from sys import path
import unittest
import xmlrunner

# Project paths
base_path = getcwd()

path.insert(0, join(base_path, 'app'))


def discover_test_cases():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_loader.discover(join(base_path, 'TestCases'), 'test_*.py'))
    return test_suite


runner = xmlrunner.XMLTestRunner(output='TestResults')
result = runner.run(discover_test_cases())
