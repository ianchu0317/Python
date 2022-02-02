'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
def modify_string(string):
    if string.endswith('ing'):
        string += 'ly'
    else:
        string += 'ing'
    return string


def main():
    # Enter data
    string = input("Input string: ")

    #Debug
    print("Entered string is '{0}'".format(string))

    if len(string) < 3:
        print("[!] String length should be more than 3 chars")
        print("Unchanged string is: '{0}'".format(string))
        exit()

    string = modify_string(string)

    print("Modified string is '{0}'".format(string))
    

if __name__ == '__main__':
    main()
