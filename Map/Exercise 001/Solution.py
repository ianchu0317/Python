# Write a Python program to triple all numbers of a giben list of integers. Use python map.


if __name__ == '__main__':
	my_list = [1, 2, 3, 4, 5]
	print("List is : ", my_list)

	my_list = list(map(lambda x: x*3, my_list))
	print("Elements multiplied by 3 is : ", my_list)
