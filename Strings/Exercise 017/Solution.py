# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses


def insert_end(string):
    if len(string) < 2:
        print("Length must be at least 2 chars")
        return

    new_string = str()
    for x in range(4):
        new_string += string[-2:]

    return new_string

if __name__ == '__main__':
    new_string = insert_end('Python')
    print(new_string)
