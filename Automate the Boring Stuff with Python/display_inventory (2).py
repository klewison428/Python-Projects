def displayInventory(inventory):
	print("Inventory:\n")
	item_total = 0
	for k, v in inventory.items():
		print(v': ', k)

	print("Total number of items: " + str(item_total))


inventory = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger': 1, 'arrow':12}
displayInventory(inventory)