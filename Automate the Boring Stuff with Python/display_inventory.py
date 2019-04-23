def displayInventory(inventory):
	print("Inventory:\n")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v

	print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
	# loop through the list, dragonLoot, and grab the items/content of the list and assign each value to item
	for item in addedItems:
		# use the item value as the key for the dictionary and set it equal to the dictionary and get the key value pair if it exists and add 1
		inventory[item] = inventory.get(item, 0) + 1
	# return the value to pass into the displayInventory function
	return inventory

if __name__ = '__main__':
	inv = {'gold coin': 42, 'rope' : 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)
	displayInventory(inv)