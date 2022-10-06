from itertools import count


def compute(n):
    number = 0
    for x in range(1, n+1):
        number += pow(n, n*x)
    return number


n = input("Enter number: ")
print(compute(int(n)))
