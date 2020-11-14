"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    set_array = list(set(array))
    my_count_elem = [array.count(elem) for elem in set_array]
    my_count = max(my_count_elem)
    return f'Число {array[my_count_elem.index(my_count)]} появляется в массиве {my_count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print('First function time: ', timeit("func_1()", setup="from __main__ import func_1", number=100000))
print('Second function time: ', timeit("func_2()", setup="from __main__ import func_2", number=100000))
print('Third function time: ', timeit("func_3()", setup="from __main__ import func_3", number=100000))

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Число 1 появляется в массиве 3 раз(а)
First function time:  0.563979009999457
Second function time:  0.49147785100103647
Third function time:  0.4420466609990399
"""
