import unittest

#Test11
from test11 import is_repdigit

class is_repdigitTest(unittest.TestCase):

    def test_is_repdigit(self):
        self.assertTrue(is_repdigit(5555))

    def test_is_repdigit(self):
        self.assertTrue(is_repdigit(0))

    def test_is_repdigit(self):
        self.assertFalse(is_repdigit(5))

    def test_is_repdigit(self):
        self.assertFalse(is_repdigit(-22))

    def test_is_repdigit(self):
        self.assertFalse(is_repdigit(12345))

    
if __name__ == '__main__':
    unittest.main()

