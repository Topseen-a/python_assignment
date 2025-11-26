import unittest
import get_discount.py

class TestGetDiscount(unittest.TestCase):
    def test_that_get_discount_exist(self):
        get_discount.get_discount()

    def test_that_get_discount_returns_name_price_promotional_code(self):
        actual = get_discount.get_discount()
        expected = 
        self.assertEqual(actual,expected)
