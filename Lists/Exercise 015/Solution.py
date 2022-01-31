from random import shuffle

def main():
    my_list = ['red', 'blue', 'green', 'yellow', 'black', 'white']
    print("List is {0}".format(my_list))
    shuffle(my_list)
    print("List after shuffle is {0}".format(my_list))

if __name__ == '__main__':
    main()
