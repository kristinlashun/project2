# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 1/17/2024
"""
This file includes unit tests for the LemonadeStand.py classes.
It tests the creation of MenuItem objects, the functionality of the SalesForDay class,
and the various methods within the LemonadeStand class such as adding menu items, entering daily sales,
calculating the total sales and profits for individual items and the entire stand.
"""
import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class TestLemonadeStand(unittest.TestCase): 

    def test_menu_item_creation(self):
        lemonade = MenuItem("lemonade", 0.5, 1.5)
        self.assertEqual(lemonade.get_name(), "lemonade")
        self.assertEqual(lemonade.get_wholesale_cost(), 0.5)
        self.assertEqual(lemonade.get_selling_price(), 1.5)


if __name__ == "__main__": 
    unittest.main()
