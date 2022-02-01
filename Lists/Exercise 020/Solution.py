#  Write a Python program access the index of a list.


def main():
    #Output data
    my_list = ['a', 'b', 'c', 'd']
    print("List is {0}".format(my_list))
    try:
        #Input data
        idx = int(input(f"Input index value: "))
        #Output data
        print("Value at index '{0}' is '{1}'".format(idx, my_list[idx]))
        quit()
    except ValueError as e:
        print(e)
        exit()
    except IndexError as e:
        print("Index not found [!]")
        exit()


if __name__ == '__main__':
    main()
