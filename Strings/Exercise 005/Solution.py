'''
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''
def swap_string(string, char):
    return string[0].replace(string[0], char) + string[1:]

def main():
    # User input
    string = input("Enter two strings separated by space: ").split(" ")

    print("Entered strings are: '{0}'".format(string))

    #Swap
    temp = string[0][0]
    string[0] = swap_string(string[0], string[-1][0])
    string[-1] = swap_string(string[-1], temp)

    # Output
    print("Swapped strings are: '{0}'".format(" ".join(string)))


if __name__ == '__main__':
    main()
