# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.



if __name__ == '__main__':
    my_dict = dict()

    for x in range(1, (16)):
        my_dict[x] = x ** 2

    print("The result is : ", my_dict)
