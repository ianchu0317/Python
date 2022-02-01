# Write a Python program to flatten a shallow list.

shallow_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_list = list()
for lst in shallow_list:
    for element in lst:
        new_list.append(element)
print("Shallow list is: {0}".format(shallow_list))
print("New list is: {0}".format(new_list))
