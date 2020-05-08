import unittest

#Test3
from test11 import solutions

class solutionsTest(unittest.TestCase):

    def test_solutions(self):
        self.assertEqual(solutions(2, 5, 2), 2)
        
    def test_solutions(self):
        self.assertEqual(solutions(1, 0, 0), 1)

    def test_solutions(self):
        self.assertEqual(solutions(1, 0, 1), 0)

    def test_solutions(self):
        self.assertNotEqual(solutions(0, 5, 2), 0)

if __name__ == '__main__':
    unittest.main()
