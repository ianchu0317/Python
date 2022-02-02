

def main():
    strings = input("Enter various words in one string: ").split(" ")
    print("Strings are: '{0}'".format(strings))

    longest_word = str()
    longest_len = 0

    for word in strings:
        if len(word) > longest_len:
            longest_word = word
            longest_len = len(word)

    print("Longest word: '{0}'".format(longest_word))
    print("Length of the longest word: '{0}'".format(longest_len))
if __name__ == '__main__':
    main()
