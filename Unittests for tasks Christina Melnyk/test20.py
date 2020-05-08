import unittest

#Task 20
from test11 import dice_game

class dice_gameTest(unittest.TestCase):

    def test_dice_game(self):
        self.assertEqual(dice_game([(1, 2), (2, 6), (3, 5)]), 19)

    def test_dice_game(self):
        self.assertEqual(dice_game([(6, 4), (3, 6), (5, 5)]), 0)

    def test_dice_game(self):
        self.assertEqual(dice_game([(1, 6), (2, 1), (3, 1)]), 13)

    def test_dice_game(self):
        self.assertEqual(dice_game([(5, 2), (4, 6), (6, 5)]), 28)

    def test_dice_game(self):
        self.assertNotEqual(dice_game([(1, 2), (2, 2), (3, 5)]), 19)

    def test_dice_game(self):
        self.assertNotEqual(dice_game([(1, 2), (2, 3), (3, 4)]), 6)

if __name__ == '__main__':
    unittest.main()

