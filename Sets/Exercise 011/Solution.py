# Write a Python program to create a shallow copy of sets


if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    print("Set 1 is : ", set1)
    set2 = set1.copy()
    print("Set 2 is : ", set2)
    set3 = {item for item in set1}
    print("Set 3 is : ", set3)
