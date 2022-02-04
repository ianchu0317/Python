
def func(n):
    return lambda x: x * n

if __name__ == '__main__':
    formula = func(2)
    print("Double of 16 is", formula(16))
