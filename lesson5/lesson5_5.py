try:
    with open('5_5_create.txt', 'w+') as f:
        number_string = input('Введите числа через пробел, для записи их в файл: ')
        f.write(number_string)
except IOError:
    print('Ошибка ввода-вывода')
try:
    with open('5_5_create.txt', 'r') as f:
        number_sum = sum(map(int, f.readline().strip().split()))
        print(f'Сумма введённых чисел составляет: {number_sum}')
except IOError:
    print('Ошибка ввода-вывода')
except ValueError:
    print('Необходимо вводить числа через пробел')
