"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def timer(func):
    def wrapper(args_for_function):
        start = time.time()
        func(args_for_function)
        end = time.time()
        print(f'func {func} takes {end - start} seconds for {args_for_function} elements')

    return wrapper


@timer
def create_list(n: int):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


@timer
def create_dict(n: int):
    my_dict = dict()
    for i, j in enumerate(range(n)):
        my_dict[i] = j
    return my_dict


number = 1000000
create_list(number)
create_dict(number)
# Вывод: заполнение словаря занимает в 1,5 - 2 раза больше времени, и она не зависит от количества элементов, что говорит о том, что сложность данных функций одинакова (О(n)). Но так как при создании словаря немного больше действий (ф-ция enumerate), то время заполнения словаря дольше.