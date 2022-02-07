#  Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map



if __name__ == '__main__':
	my_list = [1, 2, 3, 4, 5]
	index = [x for x in range(len(my_list))]
	power = list(map(pow, my_list, index))

	print("List is: ", my_list)
	print("Index is: ", index)
	print("New list is: ", power)
