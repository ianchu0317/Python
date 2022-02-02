# Input: https://www.w3resource.com/python-exercises
# Output: https://www.w3resource.com/python

from string import punctuation

def remove_last(string):
    last_part_string = str()

    for x in range(1, len(string)+1):
        last_part_string = string[-x] + last_part_string
        if string[-x] in punctuation:
            break

    return last_part_string

if __name__ == '__main__':
    print(remove_last('https://www.w3resource.com/python-exercises'))
