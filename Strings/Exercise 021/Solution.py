# Write a Python function to convert a given string to all uppercase
# if it contains at least 2 uppercase characters in the first 4 characters.

def convert_case(string):
    counter = 0
    for char in string[:4]:
        if char.isupper():
            counter += 1
    if counter < 2:
        return string
    return string.upper()


if __name__ == '__main__':
    print(convert_case("TEsting"))
    print(convert_case("Python"))
