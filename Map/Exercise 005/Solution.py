# Write a Python program to square the elements of a list using map() function.


if __name__ == '__main__':
	my_list = [1, 2, 3, 4, 5]
	print("List is : ", my_list)

	my_list = list(map(lambda x: x**2, my_list))
	print("Square of elements is : ", my_list)

