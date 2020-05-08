import unittest

#Test5
from test11 import list_of_multiples

class list_of_multiplesTest(unittest.TestCase):

    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(7, 5), [7, 14, 21, 28,35])

    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(0, 3), [0, 0, 0])

    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(3, 10), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_list_of_multiples(self):
        self.assertNotEqual(list_of_multiples(2, 5), [2, 4 ,6 ,8, 10, 12])

    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(2, 0), [])

if __name__ == '__main__':
    unittest.main()

