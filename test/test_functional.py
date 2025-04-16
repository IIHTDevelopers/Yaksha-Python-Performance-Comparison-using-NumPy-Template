import unittest
import numpy as np
from mainclass import PerformanceComparison
from test.TestUtils import TestUtils
import pandas as pd


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.performance = PerformanceComparison(size=1000000)

    def test_sum_lists(self):
        test_obj = TestUtils()
        try:
            """Test if sum of Python lists is correct"""
            result = self.performance.sum_lists()
            
            if len(result) == 1000000:
                test_obj.yakshaAssert("TestSumLists", True, "functional")
                print("TestSumLists = Passed")
            else:
                test_obj.yakshaAssert("TestSumLists", False, "functional")
                print("TestSumLists = Failed")
        except:
            test_obj.yakshaAssert("TestSumLists", False, "functional")
            print("TestSumLists = Failed")
        

    def test_sum_arrays(self):
        """Test if sum of NumPy arrays is correct"""
        test_obj = TestUtils()
        try:
            result = self.performance.sum_arrays()
            
            if len(result) == 1000000:
                test_obj.yakshaAssert("TestSumArrays", True, "functional")
                print("TestSumArrays = Passed")
            else:
                test_obj.yakshaAssert("TestSumArrays", False, "functional")
                print("TestSumArrays = Failed")
        except:
            test_obj.yakshaAssert("TestSumArrays", False, "functional")
            print("TestSumArrays = Failed")

    def test_measure_time(self):
        """Test if time is measured correctly"""
        test_obj = TestUtils()
        try:
            list_time, array_time = self.performance.measure_time()
            
            if list_time > 0 and array_time > 0:
                test_obj.yakshaAssert("TestMeasureTime", True, "functional")
                print("TestMeasureTime = Passed")
            else:
                test_obj.yakshaAssert("TestMeasureTime", False, "functional")
                print("TestMeasureTime = Failed")
        except:
            test_obj.yakshaAssert("TestMeasureTime", False, "functional")
            print("TestMeasureTime = Failed")