



def main():
    sentence = input("Enter a sentence: ").split(" ")

    new_sentence = []
    new_word = ""

    # Change sentence case
    for word in sentence:
        for char in word:
            if char.islower():
                new_word += char.upper()
            else:
                new_word += char.lower()
        new_sentence.append(new_word)
        new_word = ""

    # Output
    print("The modified sentence is: '{0}'".format(" ".join(new_sentence)))



if __name__ == '__main__':
    main()
