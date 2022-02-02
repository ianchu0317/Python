# Write a Python program to remove the nth index character from a nonempty string.
def replace_string(string, nth):
    return string[:nth-1] + string[nth:]


def main():
    string = input("Input string: ")
    nth = int(input("Input index to remove: "))

    print("Original string is : '{0}'".format(string))
    string = replace_string(string, nth)

    print("Removed {0}th char and the result is '{1}'".format(nth, string))



if __name__ == '__main__':
    main()
