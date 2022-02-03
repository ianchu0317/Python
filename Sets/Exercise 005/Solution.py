


set1 = {1, 2, 3, 4, 5}
print("Set 1 is {0}".format(set1))
element_to_remove = int(input("Input element to remove: "))

if element_to_remove not in set1:
    print("Element is not in the set1 !!!")
    exit()

set1.discard(element_to_remove)
print("Set after removing {0} is {1}".format(element_to_remove, set1))
