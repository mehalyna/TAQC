import unittest

#Test1
from test11 import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")

    def test_fizz(self):
        self.assertEqual(FizzBuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(FizzBuzz(5), "Buzz")

    def test_num(self):
        self.assertEqual(FizzBuzz(4), 4)

    def test_num(self):
        self.assertEqual(FizzBuzz(-2), -2)
    

if __name__ == '__main__':
    unittest.main()
