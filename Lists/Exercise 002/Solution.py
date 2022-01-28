import sys

def multiply(my_list):
    total = 1
    for item in my_list:
        total *= item
    return total

min = int(input("Input minimum number: "))
max = int(input("Input maximum number: "))
number_list = list(range(min, max+1))
result = multiply(number_list)

print("multiplication result is: ", result)
