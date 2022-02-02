# Python: Check whether a string starts with specified characters

def main():
    string = input("Enter a string: ")
    substring = input("Enter substring to check : ")

    print(string.startswith(substring))

if __name__ == '__main__':
    main()
