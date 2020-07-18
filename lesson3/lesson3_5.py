def my_func():
    result: int = 0
    while True:
        stop: int = 0
        data_user: list = input('Введите числа через пробел или символ "S": ').split()
        for i in data_user:
            if i.lower() == 's':
                stop = 1
                break
            else:
                result += int(i)
        if stop == 1:
            break
        else:
            pass
    return print(result)


my_func()