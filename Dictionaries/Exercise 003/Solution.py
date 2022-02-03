'''
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''


if __name__ == '__main__':
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}

    print("Dic1 = ", dic1)
    print("Dic2 = ", dic2)
    print("Dic3 = ", dic3)

    result = dic1 | dic2 | dic3
    print("Result is = ", result)
