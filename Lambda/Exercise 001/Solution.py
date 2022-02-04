'''
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48
'''

if __name__ == '__main__':
    add = lambda x : x + 15

    n1 = int(input("Input first number : "))
    n2 = int(input("Input second number : "))

    print("{0} + 15 is {1}".format(n1, add(n1)))
    print("{0} + 15 is {1}".format(n2, add(n2)))
