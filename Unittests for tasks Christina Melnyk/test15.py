import unittest

#Test15
from test11 import element_in_list

class element_in_listTest(unittest.TestCase):

    def test_element_in_list(self):
        self.assertEqual(element_in_list([7, 5, 9, 5, 4], 5), [1, 3])

    def test_element_in_list(self):
        self.assertEqual(element_in_list([7, 5, 9, 5, 4], 2), [])

    def test_element_in_list(self):
        self.assertEqual(element_in_list(["a", 5, "n", "u", 4], "a"), [0])

    def test_element_in_list(self):
        self.assertEqual(element_in_list(["1", 1, "#", "1", "1"], "1"), [0, 3, 4])

    def test_element_in_list(self):
        self.assertNotEqual(element_in_list(["1", 1, "#", "1", "1"], 1), [0, 3, 4])
        
if __name__ == '__main__':
    unittest.main()

