

def sort_list(current_tuple):
    return current_tuple[1]

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("List is {0}".format(my_list))
my_list.sort(key=sort_list)
print("Sorted list is {0}".format(my_list))
