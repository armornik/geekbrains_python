def my_func(x: int, y: int):
    result = 1
    for _ in range(abs(y)):
        result *= x
    return print(1/result)


my_func(2, -5)
