"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit


def list_check():
    my_list = [i for i in range(100)]
    my_list.append(100)
    my_list.extend([i for i in range(200)])
    my_list.insert(0, 1000)
    my_list.remove(199)
    my_list.pop()
    my_list.count(9)
    my_list.reverse()
    my_list.clear()


def deque_check():
    my_deque = deque([i for i in range(100)])
    my_deque.append(100)
    my_deque.extend([i for i in range(200)])
    my_deque.insert(0, 1000)
    my_deque.remove(199)
    my_deque.pop()
    my_deque.count(9)
    my_deque.reverse()
    my_deque.clear()


if __name__ == '__main__':
    print('List function time: ', timeit("list_check()", setup="from __main__ import list_check", number=20000))
    print('Deque function time: ', timeit("deque_check()", setup="from __main__ import deque_check", number=20000))

'''Вывод: даже при стандартных операциях deque быстрее
List function time:  0.8743017790002341
Deque function time:  0.8542323399997258'''
