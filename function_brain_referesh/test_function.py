import unittest
import redigested_check

class TestFunction(unittest.TestCase):
    def test_that_check_minutes_function_exist(self):
        redigested_check.check_minutes(30)

    def test_that_check_minutes_function_return_time_with_seconds_arguments(self):
        actual = redigested_check.check_minutes(30)
        expected = "30 minutes is 1800 seconds 0.5 hours"
        self.assertEqual(actual,expected)
