# Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically)
def sort_key(string):
    return string[0]

def main():
    my_list = input("Input a list separated by comma: ").split(" ")
    my_list = [word.rstrip(",") for word in my_list]

    print("The entered list is : {0}".format(my_list)) # Debug

    print("The sorted unique elements list is: {0}".format(sorted(list(set(my_list)), key=sort_key)))

if __name__ == '__main__':
    main()
