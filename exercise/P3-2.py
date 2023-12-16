def addListToDict(inventory,addItems):
    for key in addItems:
        if key in inventory.keys():
            inventory[key] += 1
        else:
            inventory[key] = 1
    return inventory

def displayInventory(dicList):
    totalItem = 0
    for k,v in dicList.items():
        print(f"{v} {k}\n")
        totalItem += v
    print(f'Total number of items: {totalItem}')

inventory={'gold coin':42,'rope':1}
addItems=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(addListToDict(inventory,addItems))
