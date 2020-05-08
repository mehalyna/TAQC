import unittest

#Test13
from test11 import empty_values

class empty_valuesTest(unittest.TestCase):

    def test_empty_values(self):
        self.assertEqual(empty_values([1, 2.54, {"one", 3}, 'sun']), [0, 0.0, set(), ''])

    def test_empty_values(self):
        self.assertIsNone(empty_values([None]))

    def test_empty_values(self):
        self.assertEqual(empty_values(['day', 'oreo', 'sun']), ['', '', ''])

    def test_empty_values(self):
        self.assertNotEqual(empty_values([1, 2.54, {"one", 3}, 'sun']), [1, 2.54, {"one", 3}, 'sun'])
        
if __name__ == '__main__':
    unittest.main()
