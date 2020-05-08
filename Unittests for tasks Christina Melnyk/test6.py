import unittest

#Test6
from test11 import converted_date

class converted_dateTest(unittest.TestCase):

    def test_converted_date(self):
        self.assertEqual(converted_date("10/25/2019"), "20192510")

    def test_converted_date(self):
        self.assertEqual(converted_date("12/31/2019"), "20193112")

    def test_converted_date(self):
        self.assertNotEqual(converted_date("2/15/2020"), "2152020")

if __name__ == '__main__':
    unittest.main()

