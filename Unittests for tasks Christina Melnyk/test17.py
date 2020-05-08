import unittest

#Task 17
from test11 import progress_day

class progress_dayTest(unittest.TestCase):

    def test_progress_day(self):
        self.assertEqual(progress_day([4, 5, 6, 7, 2, 5, 9]), 5)

    def test_progress_day(self):
        self.assertEqual(progress_day([6, 4, 2, 7, 1]), 1)

    def test_progress_day(self):
        self.assertEqual(progress_day([9, 8, 7, 6, 5]), 0)

    def test_progress_day(self):
        self.assertEqual(progress_day([4, 4, 4, 4]), 0)

    def test_progress_day(self):
        self.assertNotEqual(progress_day([4, 5, 7, 9, 12]), 2)

if __name__ == '__main__':
    unittest.main()

