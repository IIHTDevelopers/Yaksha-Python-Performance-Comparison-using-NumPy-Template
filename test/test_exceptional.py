import unittest
from mainclass import PerformanceComparison
from test.TestUtils import TestUtils
import numpy as np
import pandas as pd

class ExceptionalTests(unittest.TestCase):
    def exception_test(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("ExceptionTest", True, "exceptional")
        print("ExceptionTest = Passed")

