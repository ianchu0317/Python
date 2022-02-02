def change_string(string):
    new_string = str()
    for idx, ch in enumerate(string):
        if idx != 0 and ch == string[0]:
            new_string += ch.replace(ch, "$")
        else:
            new_string += ch
    return new_string


def main():
    string = input("Input string: ")
    print("Entered string is '{0}'".format(string))
    string = change_string(string)
    print("Changed string is : '{0}'".format(string))


if __name__ == '__main__':
    main()
