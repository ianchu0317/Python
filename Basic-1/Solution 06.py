data = input("Enter sequence: ")

my_list = [int(x) for x in data.strip(" ").split(",")]
my_tuple = tuple(my_list)

if __name__ == "__main__":
    print(my_list)
    print(my_tuple)
