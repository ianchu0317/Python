def Remove(my_list):
    item_1 = my_list[0]
    item_2 = my_list[4]
    item_3 = my_list[5]
    print(type(my_list))
    return my_list.remove(item_1).remove(item_2).remove(item_3)


if __name__ == '__main__':
    my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print("List is: {0}".format(my_list))
    my_list = Remove(my_list)
    print("List after removing 0th, 4th, 5th is {0}".format(my_list))
