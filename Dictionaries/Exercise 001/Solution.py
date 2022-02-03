# Sort list ascending and descending according to value

def sort_key(element):
    return element[1]

if __name__ == '__main__':

    my_dict = {"Red": 1,
               "Blue" : 3,
               "Yellow" : 2,
               "Black": 5,
               "Green" : 4,
               "Grey" : 7,
               "Brown" : 6}

    print("Dictionary is : ", my_dict)

    for element in my_dict:
        print(element[1])
    # Ascending order
    print("Ascending order of dictionary is : {0}".format(dict(sorted(my_dict.items(), key=sort_key))))

    # Descending order
    print("Descending order of dictionary is : {0}".format(dict(sorted(my_dict.items(), key=sort_key, reverse=True))))
