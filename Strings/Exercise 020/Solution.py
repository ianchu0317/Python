# Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(string):
    if len(string) % 4 != 0:
        return
    new_string = str()
    for x in range(1, len(string)+1):
        new_string += string[-x]
    return new_string

if __name__ == '__main__':
    print(reverse_string('Testings'))
