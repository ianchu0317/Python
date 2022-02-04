'''
Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

if __name__ == '__main__':
    my_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
               {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
               {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

    print("List is : ", my_list)

    print("Sorted list by color in dictionary :\n", sorted(my_list, key=lambda item: item['color']))
    
