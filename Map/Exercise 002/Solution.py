# Write a Python program to add three given lists using Python map and lambda


if __name__ == '__main__':
	list1 = [1, 2, 3, 4, 5]
	list2 = [2, 3, 4, 5, 6]
	list3 = [3, 4, 5, 6, 7]

	# Output original lists
	print("List 1 is: ", list1)
	print("List 2 is: ", list2)
	print("List 3 is: ", list3)

	# Add
	#new_list = [x + y + z for (x, y, z) in (list1, list2, list3)]
	new_list = list(map(lambda x, y , z: x+y+z, list1, list2, list3))
	print("New list is ", new_list)
