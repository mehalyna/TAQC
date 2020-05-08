import unittest

#Test7
from test11 import lines_are_parallel

class lines_are_parallelTest(unittest.TestCase):

    def test_lines_are_parallel(self):
        self.assertTrue(lines_are_parallel([1, 2, 3], [1, 2, 4]))

    def test_lines_are_parallel(self):
        self.assertTrue(lines_are_parallel([2, 4, 8], [3, 6, 8]))

    def test_lines_are_parallel(self):
        self.assertFalse(lines_are_parallel([2, 3, 4], [1, 2, 4]))
    
    def test_lines_are_parallel(self):
        self.assertFalse(lines_are_parallel([2, 5, 1], [4, 50, 1]))

if __name__ == '__main__':
    unittest.main()

