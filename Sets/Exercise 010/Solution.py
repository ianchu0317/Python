# Check if a set is a subset of another set


if __name__ == '__main__':
    #Test1
    print("Output 1")
    set1 = {1, 2, 3, 4}
    set2 = {1, 2, 3, 4, 5}
    print("Set 1 is : ", set1)
    print("Set 2 is : ", set2)
    print("Is subset ? ", set1 <= set2)

    # Test2
    print("\nOutput 2")
    set1 = {1, 4, 2, 8}
    set2 = {1, 2, 3, 4, 5}
    print("Set 1 is : ", set1)
    print("Set 2 is : ", set2)
    print("Is subset ? ", set1 <= set2)
