import unittest

#Test4
from test11 import square_area

class square_areaTest(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(2), 8)

    def test_square_area(self):
        self.assertEqual(square_area(1), 2)

    def test_square_area(self):
        self.assertEqual(square_area(12), 288)

    def test_square_area(self):
        self.assertNotEqual(square_area(2), 0)

if __name__ == '__main__':
    unittest.main()

