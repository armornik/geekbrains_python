"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_2(i):
    prime_numbers = [x for x in range(2, i * 10) if all(x % y != 0 for y in range(2, x))]
    return prime_numbers[i-1]

i = int(input('Введите порядковый номер искомого простого числа: '))

print(simple_2(i))
print(simple(i))
print('First function time: ', timeit("simple(i)", setup="from __main__ import simple, i", number=10000))
print('Second function time: ', timeit("simple_2(i)", setup="from __main__ import simple_2, i", number=10000))

