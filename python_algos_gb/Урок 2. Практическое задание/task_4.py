"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_numbers(my_number=float('nan'), num=0, my_sum=1, result=0):
    if my_number != my_number:
        try:
            my_number = int(input('Введите количество элементов: '))
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            return sum_numbers(my_number=float('nan'), num=0, my_sum=1, result=0)
    if num == my_number:
        print(result)
        return
    else:
        num += 1
        result += my_sum
        my_sum /= -2
        return sum_numbers(my_number, num, my_sum, result)


sum_numbers()
