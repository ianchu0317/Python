
def main():
    #Visualize data
    my_list = ['p', 'y', 't', 'h', 'o', 'n']
    print("List is {0}".format(my_list))
    #Conversion
    string = "".join(my_list)
    string = string.capitalize()

    #Output
    print("String converted from string is '{0}'".format(string))


if __name__ == '__main__':
    main()
