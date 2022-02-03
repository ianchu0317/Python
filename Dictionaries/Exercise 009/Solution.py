if __name__ == '__main__':
    my_dict = {"Red": 1, "Yellow": 3, "Blue": 2}
    print("Dictionary is : ", my_dict)

    print("\nPrint items separately is: ")
    for key, value in my_dict.items():
        print("{0} : {1}".format(key, value))
