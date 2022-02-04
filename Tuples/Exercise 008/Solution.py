from copy import copy

if __name__ == '__main__':
    t = ("test", 1, [], {1, 2, 3})

    print("Original tuple is : ", t)

    t_copy = copy(t)
    t_copy[2].append("Test")
    print("Copy of the tuple is : ", t_copy)
