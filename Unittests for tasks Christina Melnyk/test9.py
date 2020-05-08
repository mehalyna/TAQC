import unittest

#Test9
from test11 import greeting

class greetingTest(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(greeting("Randy"), "Hi! I'm Randy, and I'm from Germany")

    def test_greeting(self):
        self.assertEqual(greeting("Wendy"), "Hi! I'm Wendy, and I'm from Japan")
        
    def test_greeting(self):
        self.assertEqual(greeting("Kate"), "Hi! I'm a guest.")
        
    def test_greeting(self):
        self.assertEqual(greeting("123"), "Hi! I'm a guest.")

    def test_greeting(self):
        self.assertEqual(greeting("France"), "Hi! I'm a guest.")

    def test_greeting(self):
        self.assertNotEqual(greeting("Karla"), "Hi! I'm a guest.")

    def test_greeting(self):
        self.assertNotEqual(greeting("Norman"), "Hi! I'm Norman, and I'm from Japan")

    def test_greeting(self):
        self.assertNotEqual(greeting("Norman"), "Hi! I'm Randy, and I'm from England")
     
if __name__ == '__main__':
    unittest.main()
