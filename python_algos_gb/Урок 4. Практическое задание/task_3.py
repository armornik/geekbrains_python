"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


n = 10000000000

print('First function time with timeit: ', timeit("revers(n)", setup="from __main__ import revers, n", number=10000))
print('Second function with timeit: ', timeit("revers_2(n)", setup="from __main__ import revers_2, n", number=10000))
print('Third function with timeit: ', timeit("revers_3(n)", setup="from __main__ import revers_3, n", number=10000))

print('Analise with help cProfile:')
cProfile.run('revers(n), revers_2(n), revers_3(n)')


def revers_loop():
    for _ in range(10000):
        revers(n)


def revers_2_loop():
    for _ in range(10000):
        revers_2(n)


def revers_3_loop():
    for _ in range(10000):
        revers_3(n)


print('Analise with help cProfile 10 000 times:')
cProfile.run('revers_loop(), revers_2_loop(), revers_3_loop()')

# Третья ф-ция самая быстрая, так как сложность алгоритма самая маленькая (O(n) - срез)
