'''        
    Create a function called inventory_management that takes in three parameters:

    inventory: a dictionary representing current inventory where the keys 
    are item names and the values are the quantity in stock.

    item: a string representing the name of an item.

    quantity: an integer representing the number of items to be added or removed.
    This should have a default value of 1.

    transaction_type: a string representing the type of transaction 
    - either 'add' or 'remove'. This should have a default value of 'add'.
'''
def inventory_management(inventory, item, quantity=1, transaction_type='add'):
    if transaction_type == 'add':
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    elif transaction_type == 'remove':
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            if inventory[item] == 0:
                del inventory[item]
        else:
            print(f"Error: Not enough {item} in inventory to remove.")
    else:
        print("Error: Invalid transaction type.")
    print(inventory)

inventory_management({'apples': 5, 'bananas': 3}, 'apples', 3, 'remove')
inventory_management({'apples': 5, 'bananas': 3}, 'oranges')
