# Write a Python program to unpack a tuple in several variables.


if __name__ == '__main__':
    t = 1, 2, 3
    print("Tuple is '{0}'".format(t))

    a, b, c = t
    print("First element is : ", a)
    print("Second element is : ", b)
    print("Third element is : ", c)
