import unittest

#Test2
from test11 import profit

class profitTest(unittest.TestCase):

    def test_profit(self):
        self.assertEqual(profit({ "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}), 14796) 
        
    def test_profit(self):
        self.assertEqual(profit({ "cost_price": 9.21, "sell_price": 11.37, "inventory": 340}), 734) 
        
    def test_profit(self):
        self.assertEqual(profit({ "cost_price": 9.21, "sell_price": 11.37, "inventory": 0}), 0) 

    def test_profit(self):
        self.assertNotEqual(profit({ "cost_price": 123.3, "sell_price": 185.9, "inventory": 2000}), 0) 

if __name__ == '__main__':
    unittest.main()

