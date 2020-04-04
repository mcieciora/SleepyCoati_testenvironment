from os import getcwd, getenv
from os.path import join
from sys import path
import unittest
import xmlrunner

# Jenkins variables
scope = getenv('scope')

# Project paths
base_path = getcwd()

path.insert(0, join(base_path, 'app'))

patterns_list = ['smoke_*.py', 'test_*.py']
if scope == 'smoke':
    patterns_list = ['smoke_*.py']
if scope == 'regression':
    patterns_list = ['reg_*.py']


def discover_test_cases():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    for pattern in patterns_list:
        test_suite.addTest(test_loader.discover(join(base_path, 'TestCases'), pattern))
    return test_suite


runner = xmlrunner.XMLTestRunner(output='TestResults')
result = runner.run(discover_test_cases())
