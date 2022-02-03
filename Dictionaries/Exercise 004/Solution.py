# Check dictionary if has key

if __name__ == '__main__':

    my_dict = {"Red": 1,
               "Blue" : 3,
               "Yellow" : 2,
               "Black": 5,
               "Green" : 4,
               "Grey" : 7,
               "Brown" : 6}

    print("Dictionary is : ", my_dict)

    check_key = input("Enter a key to check if its in the dictionary: ")

    print("Does {0} in the dictionary ?  {1}".format(check_key, check_key in my_dict))
