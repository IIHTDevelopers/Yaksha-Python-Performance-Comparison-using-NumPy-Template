import unittest
import numpy as np
from mainclass import PerformanceComparison
from test.TestUtils import TestUtils
import pandas as pd


class BoundaryTests(unittest.TestCase):
    def test_single_element(self):
        """Test with single element in data structures"""
        test_obj = TestUtils()
        try:
            performance_single = PerformanceComparison(size=1)
            list_time, array_time = performance_single.measure_time()
        
            if list_time > 0 and array_time > 0:
                test_obj.yakshaAssert("TestSingleElement", True, "boundary")
                print("TestSingleElement = Passed")
            else:
                test_obj.yakshaAssert("TestSingleElement", False, "boundary")
                print("TestSingleElement = Failed")
        except:
            test_obj.yakshaAssert("TestSingleElement", False, "boundary")
            print("TestSingleElement = Failed")

    def test_large_data(self):
        """Test with very large data to check performance scaling"""
        test_obj = TestUtils()
        try:
            performance_large = PerformanceComparison(size=10000000)  # 10 million
            list_time, array_time = performance_large.measure_time()
            
            if list_time > 0 and array_time > 0:
                test_obj.yakshaAssert("TestLargeData", True, "boundary")
                print("TestLargeData = Passed")
            else:
                test_obj.yakshaAssert("TestLargeData", False, "boundary")
                print("TestLargeData = Failed")
        except:
            test_obj.yakshaAssert("TestLargeData", False, "boundary")
            print("TestLargeData = Failed")