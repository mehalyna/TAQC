import unittest

#Test23
from test11 import last_digit

class last_digitTest(unittest.TestCase):

    def test_last_digit(self):
        self.assertTrue(last_digit(21, 25, 125))

    def test_last_digit(self):
        self.assertTrue(last_digit(1, 123, 3243))

    def test_last_digit(self):
        self.assertTrue(last_digit(21, 0, 10))

    def test_last_digit(self):
        self.assertTrue(last_digit(28, 237, 46))

    def test_last_digit(self):
        self.assertFalse(last_digit(2, 3, 4))

    def test_last_digit(self):
        self.assertFalse(last_digit(0, 5, 342))


        
if __name__ == '__main__':
    unittest.main()

