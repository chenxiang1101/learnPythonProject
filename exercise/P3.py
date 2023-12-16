def displayInventory(dicList):
    for k,v in dicList.items():
        print(f"{v} {k}\n")
dicList={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(dicList)