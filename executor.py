from os import getcwd, environ
from os.path import join
from sys import path
import unittest
import xmlrunner

# Project paths
base_path = getcwd()
components = environ['components']
path.insert(0, join(base_path, 'app'))


def discover_test_cases(sub_test_case):
    try:
        test_loader = unittest.TestLoader()
        test_suite = unittest.TestSuite()
        if sub_test_case != '':
            test_suite.addTest(test_loader.discover(join(base_path, 'TestCases', sub_test_case), 'test_*.py'))
        return test_suite
    except ImportError:
        return unittest.TestSuite()


def get_components():
    return components.split(',')


for component in get_components():
    runner = xmlrunner.XMLTestRunner(output='TestResults')
    result = runner.run(discover_test_cases(component))
