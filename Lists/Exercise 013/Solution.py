'''
list format:
[[][][][][][]] [[][][][][][]] [[][][][][][]]
[][][]
[][][]
'''

def main():
    my_list = [[['*' for col in range(1, 6+1)] for col in range(1, 4+1)] for row in range(1, 3+1)]

    print(my_list)

if __name__ == '__main__':
    main()
