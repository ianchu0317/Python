

def remove_duplicate(my_list):
    for item in my_list:
        if my_list.count(item) > 1:
            del my_list[my_list.index(item)]
    return my_list

my_list = ['Red', 'Green', 'Yellow', 'Blue', 'Red', 'Blue']

print("The original list is: {0}".format(my_list))
print("Removed duplicated list is: {0}".format(remove_duplicate(my_list)))
