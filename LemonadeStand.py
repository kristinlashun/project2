# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 1/17/2024

"""
Description: Implementation of three classes: MenuItem, SalesForDay, and LemonadeStand.
The MenuItem class models a menu item with its name, wholesale cost, and selling price.
The SalesForDay class tracks the sales of items for a specific day.
The LemonadeStand class represents the lemonade stand itself, managing its menu items, daily sales, and calculating profits.
Includes a main function to demonstrate creation of a LemonadeStand object, adding menu items, and handling daily sales with a custom exception for invalid sales items.
"""

class InvalidSalesItemError(Exception):
    pass 

class MenuItem: 
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name 
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name
    
    def get_wholesale_cost(self):
        return self._wholesale_cost
    
    def get_selling_price(self): 
        return self._selling_price
    

class SalesForDay: 
    def __init__(self, day, sales_dict):
        self._day = day 
        self._sales_dict = sales_dict 

    def get_day(self): 
        return self._day
    
    def get_sales_dict(self):
        return self._sales_dict
    

class LemonadeStand:
    def __init__(self, name): 
        self._name = name 
        self._current_day = 0 
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        return self._name

    def add_menu_item(self, menu_item):
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        for item in sales_dict: 
            if item not in self._menu: 
                raise InvalidSalesItemError(f"Invalid item: {item}")
        self._sales_record.append(SalesForDay(self._current_day, sales_dict))
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        for sales in self._sales_record:
            if sales.get_day() == day:
                return sales.get_sales_dict().get(item_name, 0)
        return 0

    def total_sales_for_menu_item(self, item_name):
        return sum(sales.get_sales_dict().get(item_name, 0) for sales in self._sales_record)

    def total_profit_for_menu_item(self, item_name):
        item = self._menu.get(item_name)
        if item:
            sales = self.total_sales_for_menu_item(item_name)
            return sales * (item.get_selling_price() - item.get_wholesale_cost())
        return 0

    def total_profit_for_stand(self):
        return sum(self.total_profit_for_menu_item(item.get_name()) for item in self._menu.values())

# This is the main function that runs if the file is run as a script. 
def main(): 
    stand = LemonadeStand("Lemons R Us")
    # creating some menu items
    items = [
        MenuItem("lemonade", 0.5, 1.5),
        MenuItem("nori", 0.6, 0.8), 
        MenuItem("cookie", 0.2, 1)
    ]
    # Add items to the stand's menu 
    for item in items: 
        stand.add_menu_item(item)

    # creating a dictionary of sales for the day 
    sales_dict = {
        "lemonade": 5, 
        "cookie": 2, 
        "invalid_item": 1  # This item is not in the menu
    }

    try: 
        stand.enter_sales_for_today(sales_dict)
    except InvalidSalesItemError as e: 
        print(e)

if __name__ == "__main__": 
    main()
