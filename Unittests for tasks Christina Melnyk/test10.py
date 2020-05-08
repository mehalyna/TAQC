import unittest

#Test10
from test11 import stupid_addition

class stupid_additionTest(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(stupid_addition(1, 2), "12")

    def test_greeting(self):
        self.assertEqual(stupid_addition("1", "2"), 3)

    def test_greeting(self):
        self.assertIsNone(stupid_addition(1, "2"))

    def test_greeting(self):
        self.assertEqual(stupid_addition(5321, 124352), "5321124352")

    def test_greeting(self):
        self.assertEqual(stupid_addition("43", "762"), 805)

    def test_greeting(self):
        self.assertNotEqual(stupid_addition(3, 2), 5)

    def test_greeting(self):
        self.assertNotEqual(stupid_addition(3, 3), 5)

    def test_greeting(self):
        self.assertIsNotNone(stupid_addition("1", "2"))

if __name__ == '__main__':
    unittest.main()

