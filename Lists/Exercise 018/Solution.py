from itertools import permutations

def main():
    my_list = ['a', 'b', 'c', 'd', 'e']
    print("The list is {0}\n".format(my_list))

    print("Permutations are: ")
    for p in permutations(my_list):
        print(list(p))


if __name__ == '__main__':
    main()
