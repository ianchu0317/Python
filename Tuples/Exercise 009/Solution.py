# Write Python program to find the repeated items of a tuple



if __name__ == '__main__':
    t = 1, 2, 3, 4, 5, 3, 4

    print("Tuple is ", t)
    repeated = [item for item in t if t.count(item) > 1]
    print("Repeated items are: ", repeated)
