'''
 Write a Python program to generate and print a list of first and last 5 elements
 where the values are square of numbers between 1 and 30 (both included)
'''

def print_square(my_list):
    for element in my_list:
        print("Sq of {0} : {1}".format(element, pow(element, 2)))

def main():
    max = int(input("Input max range: ")) + 1
    my_list = [x for x in range(1, max)]
    #Output
    print("List is {0}".format(my_list))
    #First 5 elements
    print("\nFirst elements are: {0}".format(my_list[:5]))

    #Last elements
    print("\nLast elements are:")
    print_square(my_list[5:])




if __name__ == '__main__':
    main()
