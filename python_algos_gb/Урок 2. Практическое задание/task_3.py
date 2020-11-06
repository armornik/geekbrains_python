"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def reverse_numbers(my_number=float('nan'), reverse_number=''):
    if my_number != my_number:
        try:
            my_number = int(input('Введите число, которое требуется перевернуть: '))
            my_number = str(my_number)
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            return reverse_numbers(my_number=float('nan'), reverse_number='')
    if len(my_number) == 1:
        reverse_number += my_number[0]
        print(f'Перевернутое число:  {reverse_number}')
        return

    reverse_number += my_number[-1]
    my_number = my_number[:-1]
    return reverse_numbers(my_number, reverse_number)


reverse_numbers()
