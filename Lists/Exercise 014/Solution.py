
def remove_even_numbers(my_list):
    my_list = [x for x in my_list if x % 2 != 0]
    return my_list
    
def main():
    max = int(input("Input max range: "))
    my_list = [x for x in range(max)]
    print("List is {0}".format(my_list))
    print("List after removing even number is {0}".format(remove_even_numbers(my_list)))


if __name__ == '__main__':
    main()
