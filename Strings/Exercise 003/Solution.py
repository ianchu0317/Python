'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''

def main():
    string = input("Input a string: ")
    print("String is '{0}'".format(string))
    if len(string) >= 2:
        new_string = string[:2] + string[-2:]
        print("New string is '{0}'".format(new_string))
    else:
        print("Empty string")

if __name__ == '__main__':
    main()
