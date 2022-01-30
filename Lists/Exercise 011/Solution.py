
def checkCommon(list1, list2):
    for element in list1:
        for element_2 in list2:
            print("Comparing: {0} == {1}".format(element, element_2))
            if element == element_2:
                return True
        print()

def main():
    # Define list
    list1 = ['Red', 'Blue', 'Green', 'Orange', 'Yellow']
    list2 = ['Yellow', 'Grey', 'Violet', 'Black', 'White']

    # Output list
    print("List 1 is: {0}".format(list1))
    print("List 2 is: {0}".format(list2))

    # Check if list have common
    haveCommon = checkCommon(list1, list2)

    print(haveCommon)

if __name__ == '__main__':
    main()
