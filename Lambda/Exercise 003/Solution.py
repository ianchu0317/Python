'''
Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''


if __name__ == '__main__':
    my_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    print("List is ", my_list)
    print("Sorted list is : ", sorted(my_list, key = lambda item: item[1]))
