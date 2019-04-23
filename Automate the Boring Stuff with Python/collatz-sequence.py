def collatz(number):
	if(number % 2 == 0):
		print(number // 2)
		return number
	elif(number % 2 == 1):
		print(number * 3 + 1)
		return number

print("Enter a number")
try:
	number = int(input())
	collatz(number)
except ValueError:
		print("Error: You must enter an integer.") 