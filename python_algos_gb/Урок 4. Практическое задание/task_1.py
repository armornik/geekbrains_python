"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


n = list(range(100))

print('First function time: ', timeit("func_1(n)", setup="from __main__ import func_1, n", number=10000))


def func_2(nums):
    new_arr = []
    for index, elem in enumerate(nums):
        if elem % 2 == 0:
            new_arr.append(index)
    return new_arr


print('Second function time: ', timeit("func_2(n)", setup="from __main__ import func_2, n", number=10000))

# Вместо двух встроенных функций range и len, использовал одну enumerate, тем самым уменьшил время выполнения
