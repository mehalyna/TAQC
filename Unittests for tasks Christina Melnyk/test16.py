import unittest

#Task 16
from test11 import intersecting_intervals

class intersecting_intervalsTest(unittest.TestCase):

    def test_intersecting_intervals(self):
        self.assertEqual(intersecting_intervals([[2, 5], [9, 12], [2, 4], [1, 12]], 3), 3)

    def test_intersecting_intervals(self):
        self.assertEqual(intersecting_intervals([[2, 15], [4, 12], [2, 7], [10, 12]], [8, 9], 8), 4)

    def test_intersecting_intervals(self):
        self.assertEqual(intersecting_intervals([[1, 2], [2, 4], [3, 8]], 30), 0)

    def test_intersecting_intervals(self):
        self.assertNotEqual(intersecting_intervals([[2, 5], [5, 7], [8, 19]], 10), 3)

if __name__ == '__main__':
    unittest.main()

