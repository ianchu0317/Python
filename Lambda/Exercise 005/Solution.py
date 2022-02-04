# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] sort odd and even numbers


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List is : ", my_list)

    # odd numbers
    print("Sorted odd numbers : ", list(filter(lambda item: item % 2 == 0, my_list)))

    # even numbers
    print("Sorted even numbers : ", list(filter(lambda item: item % 2 != 0, my_list)))
