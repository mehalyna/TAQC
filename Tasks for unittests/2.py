#Calculate the Profit
#You work for a manufacturer, and have been asked to calculate the total
#profit made on the sales of a product. You are given a dictionary
#containing the cost price per unit (in dollars), sell price per unit
#(in dollars), and the starting inventory. Return the total profit made,
#rounded to the nearest dollar. Assume all of the inventory has been sold.


def profit(dictionary):
    total_cost = dictionary["cost_price"] * dictionary["inventory"]
    total_sales = dictionary["sell_price"] * dictionary["inventory"]
    profit = total_sales - total_cost
    return (round(profit))

print(profit({"cost_price": 9.21, "sell_price": 11.37, "inventory": 340}))

