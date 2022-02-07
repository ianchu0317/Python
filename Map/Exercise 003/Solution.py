# Write a Python program to listify the list of given strings individually using Python map.

if __name__ == '__main__':

	my_list = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']
	my_list = [element.capitalize() for element in my_list]

	print("List is: ", my_list)


	my_list = list(map(lambda word: list(word), my_list))
	print("New_list is : ", my_list)
