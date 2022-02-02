'''
Python: Change a given string to a new string where the first and last chars have been exchanged
'''
def swap(string):
    temp = string[0]
    return string[-1] + string[1:-1] + string[0]

def main():
    string = input("Input string: ")
    print("String '{0}'".format(string))
    string = swap(string)
    print("Swapped string is '{0}'".format(string))


if __name__ == '__main__':
    main()
