# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_three(string):
    return string[:3] if len(string) > 3 else string

if __name__ == '__main__':
    print(first_three('python'))
