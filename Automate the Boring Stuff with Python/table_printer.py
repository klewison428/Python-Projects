def printTable():
	colWidths = [0] * len(tableData)
	for column in tableData:
		for row in column:
			if len(colWidths) < len(row):
				print("column widths = " + str(colWidths))
				print("row = " + str(row))
				longest_word = len(row)
				longest_word = row
		print(longest_word)


tableData = [['apples', 'oranges', 'cherries', 'banana'], #[0][0] = giving me apples
		['Alice', 'Bob', 'Carol', 'David'], #[0][1]
		['dogs', 'cats', 'moose', 'goose']] #[0][2]
printTable()

# need to compare the longest word with the 
# if this longest word is greater than that longest word update colWidths with the longest one