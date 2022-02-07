# Write a Python program to add two given lists and find the difference between lists. Use map() function.

def add(n1, n2):
	return n1 + n2

def substract(n1, n2):
	return n1 - n2

if __name__ == '__main__':
	list1 = [4, 5, 6, 7, 8, 9]
	list2 = [1, 2, 3, 4, 5, 6]

	added_elements = list(map(add, list1, list2))
	substracted_elements = list(map(substract, list1, list2))

	print("Add of list is ", added_elements)
	print("Difference of lists are: ", substracted_elements)
