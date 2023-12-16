inv = { 'gold coin':42, 'rope':1,'torch':6,'dagger':1,'arrow':12}

def dispalyInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f'Total number of items: {item_total}' )
dispalyInventory(inv)