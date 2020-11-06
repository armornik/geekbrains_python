"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def odd_even(my_number=float('nan'), odd_sum=[], even_sum=[]):
    if my_number != my_number:
        try:
            my_number = int(input('Введите число:'))
            my_number = str(my_number)
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            return odd_even(my_number=float('nan'), odd_sum=[], even_sum=[])
    if len(my_number) == 1:
        odd_sum.append(int(my_number[0]) % 2 == 0)
        even_sum.append(int(my_number[0]) % 2 == 1)
        my_list = (sum(odd_sum), sum(even_sum))
        print(f'Количество четных и нечетных цифр в числе равно: {my_list}')
        return

    odd_sum.append(int(my_number[0]) % 2 == 0)
    even_sum.append(int(my_number[0]) % 2 == 1)
    my_number = my_number[1:]
    return odd_even(my_number, odd_sum, even_sum)


odd_even()
