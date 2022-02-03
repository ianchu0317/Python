# Python program to create sets difference


if __name__ == '__main__':
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print("Set 1 is: ", set1)
    print("Set 2 is: ", set2)

    set3 = set1 - set2
    print("Difference of set1 and set2 is: ", set3)
    set3 = set2 - set1
    print("Difference of set2 and set1 is: ", set3)
