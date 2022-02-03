# Write a Python program to iterate over dictionaries using for loops.

if __name__ == '__main__':
    my_dict = {"Red": 1,
               "Blue" : 3,
               "Yellow" : 2,
               "Black": 5,
               "Green" : 4,
               "Grey" : 7,
               "Brown" : 6}

    print("Dictionary is : ", my_dict)

    print("\nItems printed separately are: ")
    for item in my_dict:
        print("{0} : {1}".format(item, my_dict.get(item)))
