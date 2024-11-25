#Programmer: Matthew Washburn
#Program: Retail Item Class
class RetailItem:

# initialize the attributes
    def __init__(self, description, units, price):
        self.__item_description = description
        self.__units_in_inventory = units
        self.__price = price
# set attribute data
    def set_item_description(self, description):
        self.__item_description = description

    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units

    def set_price(self, price):
        self.__price = price
# get attribute data
    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

# test RetailItem class in Retail Item_Program