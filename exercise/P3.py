def addListToDict(inventory,addItems):
    for key in addItems:
        if key in inventory.keys():
            inventory[key] += 1
        else:
            inventory[key] = 1
    return inventory

def displayInventory(dicList):
    for k,v in dicList.items():
        print(f"{v} {k}\n")

inventory={'gold coin':42,'rope':1}
addItems=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(addListToDict(inventory,addItems))
