import unittest
from main_store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        self.assertAlmostEquals(-38.57, coupon_calculations.calculate_price(8, 5, 15))


if __name__ == '__main__':
    unittest.main()
