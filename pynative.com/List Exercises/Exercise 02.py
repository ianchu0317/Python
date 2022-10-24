"""
input: 

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
"""

"""
output: 
['My', 'name', 'is', 'Kelly']
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = ["".join(word) for word in zip(list1, list2)]

print(" ".join(list3))
