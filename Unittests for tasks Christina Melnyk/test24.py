import unittest

#Test24
from test11 import count_letters

class count_lettersTest(unittest.TestCase):

    def test_count_letters(self):
        self.assertEqual(count_letters(['Sun', 'CIRcle', 'MontH', 'caT']), 8)

    def test_count_letters(self):
        self.assertEqual(count_letters(['coFFe', 'TeA', 'CUP', 'smoke']), 7)

    def test_count_letters(self):
        self.assertEqual(count_letters(['code', 'letter']), 0)

    def test_count_letters(self):
        self.assertEqual(count_letters(['CAT', 'SUN']), 6)

    def test_count_letters(self):
        self.assertNotEqual(count_letters(['CAT', 'SUN']), 3)

    def test_count_letters(self):
        self.assertNotEqual(count_letters(['CAT', 'SUN']), 0)

if __name__ == '__main__':
    unittest.main()

