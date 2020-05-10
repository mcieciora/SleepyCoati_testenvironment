from os import getcwd, environ
from os.path import join
from sys import path
import unittest
import xmlrunner

# Project paths
base_path = getcwd()
components = environ['components']
print(components)
path.insert(0, join(base_path, 'app'))


def discover_test_cases():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    for component in get_components():
        test_suite.addTest(test_loader.discover(join(base_path, 'TestCases', component), 'test_*.py'))
    return test_suite


def get_components():
    return components.split(',')


runner = xmlrunner.XMLTestRunner(output='TestResults')
result = runner.run(discover_test_cases())
