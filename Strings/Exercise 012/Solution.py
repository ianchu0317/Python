#  Write a Python program to count the occurrences of each word in a given sentence.


def main():
    # User input
    sentence = input("Enter a sentence: ").split(" ")

    counter = dict()

    print("The words in the sentence are: {0}".format(sentence))
    # Initialize counter for each element in list
    for word in sentence:
        counter[word] = 0

    # Count variables
    for word in sentence:
        counter[word] += 1

    print("Occurrence of each word: {0}".format(counter))
    

if __name__ == '__main__':
    main()
