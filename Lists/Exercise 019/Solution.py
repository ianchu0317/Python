def get_difference(list1, list2):
    #define length of string
    max = int()
    if len(list1) >= len(list2):
        max = len(list1)
    else:
        max = len(list2)

    # Loop through index
    for x in range(max):
        try:
            if list1[x] != list2[x]:
                print(f"(list1[{x}] = {list1[x]}) != (list2[{x}] = {list2[x]})")
        except IndexError as e:
            print(e)
            break


def main():
    # User input data
    list1 = list(input("Enter first string: "))
    list2 = list(input("Enter second string: "))

    print("First list is {0}".format(list1))
    print("Second list is ", list2)

    get_difference(list1, list2)


if __name__ == '__main__':
    main()
