
set1 = {1, 2, 3, 4, 5}

print("Set 1 is {0}".format(set1))
new_elements = set(input("Enter new elements separated by space: ").split(" "))
new_elements = {int(item) for item in new_elements}
set1.update(new_elements)

print("Updated set is {0}".format(set1))
