import unittest

#Test8
from test11 import volume

class volumeTest(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(volume(4, 2), 234.572)

    def test_volume(self):
        self.assertEqual(volume(5, 2.5), 458.149)

    def test_volume(self):
        self.assertEqual(volume(4, 4), 0)

    def test_volume(self):
        self.assertNotEqual(volume(3, 5), 0)
     
if __name__ == '__main__':
    unittest.main()

