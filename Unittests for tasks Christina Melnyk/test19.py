import unittest


#Task 19
from test11 import oddish_or_evenish

class oddish_or_evenishTest(unittest.TestCase):

    def test_oddish_or_evenish(self):
        self.assertEqual(oddish_or_evenish(38), "Oddish")

    def test_oddish_or_evenish(self):
        self.assertEqual(oddish_or_evenish(13), "Evenish")

    def test_oddish_or_evenish(self):
        self.assertEqual(oddish_or_evenish(112233), "Evenish")

    def test_oddish_or_evenish(self):
        self.assertNotEqual(oddish_or_evenish(20), "Evenish")

    def test_oddish_or_evenish(self):
        self.assertNotEqual(oddish_or_evenish(357), "Evenish")

if __name__ == '__main__':
    unittest.main()

