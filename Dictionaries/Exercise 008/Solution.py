# Write a Python script to merge two Python dictionaries.

if __name__ == '__main__':
    dic1 = {"Red": 1, "Yellow": 3, "Blue": 2}
    dic2 = {"Green": 2, "Red": 3, "Yellow" : 2}

    print("Dic1 is : ", dic1)
    print("Dic2 is : ", dic2)

    merged_dic = dict()

    for key, value in dic1.items():
        merged_dic[key] = value
    for key, value in dic2.items():
        merged_dic.update({key:value})

    print("Merged dictionary is : ", merged_dic)
