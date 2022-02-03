# Write a Python program to create a symmetric diference


if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 6, 7}
    print("Set1 is: ", set1)
    print("Set2 is: ", set2)

    set3 = set1.symmetric_difference(set2)
    print("Set3 is : ", set3)
