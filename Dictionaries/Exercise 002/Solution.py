# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}




if __name__ == '__main__':
    my_dict = {0: 10, 1: 20}
    print("Dictionary is : ", my_dict)
    my_dict.update({2:30})
    print("Updated dictionary is : ", my_dict)
