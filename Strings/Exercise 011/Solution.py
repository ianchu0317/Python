#  Write a Python program to remove the characters which have odd index values of a given string.

def input_string():
    string = input("Input string: ")
    return string

def output(string):
    print("The string is {0}".format(string))

def main():
    string = input_string()
    output(string)

    new_string = str()
    for x in range(len(string)):
        if x % 2 == 0:
            new_string += string[x]

    print("Output, string is '{0}'".format(new_string))


if __name__ == '__main__':
    main()
