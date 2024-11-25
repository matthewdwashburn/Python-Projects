#Programmer: Matthew Washburn
#Program: Retail Item Program

from RetailItem import RetailItem

# define main function
def main():
    item_list = []
    # add three retail items to the list.
    print('Enter data for three items.')
    for count in range(1, 4):
        # get item data
        print('Retail Item ' + str(count) + ':')
        item = input('Enter description of item: ')
        units = float(input('Enter number of units in inventory: '))
        price = float(input('Enter price of item: '))
        print()

        items = RetailItem(item, units, price)

        # add items to list
        item_list.append(items)

    # display data in the list
    print('Retail Item Data:')
    display_list(item_list)

#display item info
def display_list(item_list):
    for item in item_list:
        print(f"Description: {item.get_item_description()}")
        print(f"Inventory In Stock: {int(item.get_units_in_inventory())}")
        print(f"Price: ${item.get_price():,.2f}")
        print()

# call main function
if __name__ == "__main__":
    main()