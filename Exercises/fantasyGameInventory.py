#Program to iterate through a inventory

player_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory():
    print("Inventory:")
    total_items = 0
    for k, v in player_inventory.items():
        print(v, k)
        total_items = total_items + v
    print("Total number of items:", total_items)

displayInventory()
