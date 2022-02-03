# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



if __name__ == '__main__':
    n = int(input("Enter number: "))

    my_dict = dict()

    for x in range(1, (n+1)):
        my_dict[x] = x * x

    print("The result is : ", my_dict)
