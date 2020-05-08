import unittest

#Test25
from test11 import pandigital_numbers

class pandigital_numbersTest(unittest.TestCase):

    def test_pandigital_numbers(self):
        self.assertTrue(pandigital_numbers(1326574098))

    def test_pandigital_numbers(self):
        self.assertTrue(pandigital_numbers(1923024456262478353423344970))

    def test_pandigital_numbers(self):
        self.assertTrue(pandigital_numbers(9801237645))

    def test_pandigital_numbers(self):
        self.assertFalse(pandigital_numbers(11111111111111111243435387))

    def test_pandigital_numbers(self):
        self.assertFalse(pandigital_numbers(111222333000999888777746455546463544))

    def test_pandigital_numbers(self):
        self.assertFalse(pandigital_numbers(1231231231))
    

if __name__ == '__main__':
    unittest.main()
