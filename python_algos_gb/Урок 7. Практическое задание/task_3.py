"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint
from timeit import timeit


flag = True
while flag:
    try:
        m = int(input('Введите натуральное число: '))
        flag = False
    except ValueError:
        print('Необходимо ввести натуральное число число')


orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный список из 2 * m + 1 элементов: {orig_list}')


def median_element(a):
    k, left, right = len(a) // 2, 0, len(a) - 1
    while True:
        mid = partition(a, left, right)

        if mid == k:
            return a[mid]

        if k < mid:
            right = mid
        else:
            left = mid + 1


def partition(a, i, j):
    v = a[(i + j) // 2]
    while i <= j:
        while a[i] < v:
            i += 1
        while a[j] > v:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return j


print('Время нахождения медианного элемента: ', timeit("median_element(orig_list[:])",
                                                       setup="from __main__ import median_element, orig_list", number=1)
      )
print(f'Медианный элемент: {median_element(orig_list)}')

"""Введите натуральное число: 6
Исходный список из 2 * m + 1 элементов: [-62, -36, -71, -15, 88, 46, -61, 43, 34, 50, -46, 53, 69]
Время нахождения медианного элемента:  2.3256000076798955e-05
Медианный элемент: -36"""
