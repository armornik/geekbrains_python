"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def dict_check():
    my_dict = {i: [i] for i in range(100)}
    my_dict[100] = 100
    my_dict.pop(99)


def order_check():
    my_order = OrderedDict({i: [i] for i in range(100)})
    my_order[100] = 100
    my_order.pop(99)


if __name__ == '__main__':
    print('Dict function time: ', timeit("dict_check()", setup="from __main__ import dict_check", number=20000))
    print('Order function time: ', timeit("order_check()", setup="from __main__ import order_check", number=20000))

"""Вывод: OrderedDict медленнее обычного словаря, поэтому если используешь Python версии больше 3.5, 
где порядок словаря сохраняется, то лучше использовать обычный словарь
Dict function time:  0.4465517030002957
Order function time:  1.0542386550005176"""
