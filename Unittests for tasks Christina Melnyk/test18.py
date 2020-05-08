import unittest

#Task 18
from test11 import square_patch

class square_patchTest(unittest.TestCase):

    def test_square_patch(self):
        self.assertEqual(square_patch(3), [[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    def test_square_patch(self):
        self.assertEqual(square_patch(1), [1])

    def test_square_patch(self):
        self.assertEqual(square_patch(0), [])

    def test_square_patch(self):
        self.assertEqual(square_patch(7), [[7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7]])

    def test_square_patch(self):
        self.assertNotEqual(square_patch(3), [[3, 3, 3], [3, 3, 3]])

if __name__ == '__main__':
    unittest.main()

