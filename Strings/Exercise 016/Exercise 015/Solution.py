# Python: Insert a string in the middle of a string


def main():
    # User input data
    my_sentence = input("Enter a sentence: ")
    string = input("Enter a string to insert in the middle of the sentence: ")

    # Debug
    print("Entered sentence is '{0}'".format(my_sentence))
    print("String to insert is '{0}'".format(string))

    # Change into list
    my_sentence = my_sentence.split(" ")
    middle_position = int(len(my_sentence) / 2)
    my_sentence.insert(middle_position, string)

    # Output
    print("Modified sentence is '{0}'".format(" ".join(my_sentence)))

if __name__ == '__main__':
    main()
