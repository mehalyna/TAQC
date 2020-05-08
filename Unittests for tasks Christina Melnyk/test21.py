import unittest

#Task21
from test11 import sastry_numbers

class sastry_numbersTest(unittest.TestCase):

    def test_sastry_numbers(self):
        self.assertTrue(sastry_numbers(183))

    def test_sastry_numbers(self):
        self.assertTrue(sastry_numbers(328))

    def test_sastry_numbers(self):
        self.assertFalse(sastry_numbers(12))

    def test_sastry_numbers(self):
        self.assertTrue(sastry_numbers(0))

if __name__ == '__main__':
    unittest.main()

