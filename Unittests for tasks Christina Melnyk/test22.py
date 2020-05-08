import unittest

#Test22
from test11 import num_of_sublists

class num_of_sublistsTest(unittest.TestCase):

    def test_num_of_sublists(self):
        self.assertEqual(num_of_sublists([[2, 5], [5, 7], [8, 19]]), 3)

    def test_num_of_sublists(self):
        self.assertEqual(num_of_sublists([[2, 5, 8, 1]]), 1)

    def test_num_of_sublists(self):
        self.assertEqual(num_of_sublists([1, 2, 3, 4]), 0)

    def test_num_of_sublists(self):
        self.assertNotEqual(num_of_sublists([[2, 5], [5, 7], [8, 19]]), 12)
        
if __name__ == '__main__':
    unittest.main()

