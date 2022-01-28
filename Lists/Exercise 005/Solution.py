
def string_len_counter(my_list):
    counter = 0
    for item in my_list:
        if len(item) > 2 and item[0] == item[-1]:
            counter += 1
    return counter

items = int(input("Input items number in for the list: "))

my_list = list()
for item_no in range(1, items+1):
    my_list.append(input("Input item {0}: ".format(item_no)))

result = string_len_counter(my_list)

print("List is ", my_list)
print("Result is: ", result)
