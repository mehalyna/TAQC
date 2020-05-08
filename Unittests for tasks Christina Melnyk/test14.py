import unittest

#Test14
from test11 import sum_fractions

class sum_fractionsTest(unittest.TestCase):

    def test_sum_fractions(self):
        self.assertEqual(sum_fractions([[7,19], [1,4], [13, 8], [0,2], [15, 4]]), 6)

    def test_sum_fractions(self):
        self.assertEqual(sum_fractions([[3,5], [10,4], [45, 3]]), 18)

    def test_sum_fractions(self):
        self.assertNotEqual(sum_fractions([[12, 17], [1, 4], [10, 20]]), 10)
        
if __name__ == '__main__':
    unittest.main()

