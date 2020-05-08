import unittest

#Test12
from test11 import concat

class concatTest(unittest.TestCase):

    def test_concat(self):
        self.assertEqual(concat([1, 2], [3], [4, 5], [6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_concat(self):
        self.assertEqual(concat([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_concat(self):
        self.assertEqual(concat([1, 2, 3], [6, 7, 8]), [1, 2, 3, 6, 7, 8])

    def test_concat(self):
        self.assertNotEqual(concat([1, 2], [3], [4, 5]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_concat(self):
        self.assertNotEqual(concat([1, 2], [3], [4, 5]), ([1, 2], [3], [4, 5]))
    
if __name__ == '__main__':
    unittest.main()

