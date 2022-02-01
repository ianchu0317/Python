# Write a Python program to find the index of an item in a specified list.
import string

def main():
    my_list = list(string.ascii_letters)
    print("List is {0}".format(my_list))
    item = input("Enter item to find index: ")
    print("Value '{0}' found at index '{1}'".format(item, my_list.index(item)))
    


if __name__ == '__main__':
    main()
