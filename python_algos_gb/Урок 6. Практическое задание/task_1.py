"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# pip install memory_profiler
import platform
from memory_profiler import profile

n = list(range(100))


@profile
def func_1(nums):
    new_arr = []
    x = list(range(10000))
    zn = list(range(10000))
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile()
def func_2(nums):
    new_arr = []
    cx = list(range(10000))
    czn = list(range(10000))
    for index, elem in enumerate(nums):
        if elem % 2 == 0:
            new_arr.append(index)
    return new_arr


@profile()
def func_3(nums):
    new_arr = []
    cx1 = list(range(20000))
    czn1 = list(range(20000))
    for index, elem in enumerate(nums):
        if elem % 2 == 0:
            new_arr.append(index)
    return new_arr


@profile()
def func_4(nums):
    new_arr = []
    cx2 = list(range(20000))
    czn2 = list(range(20000))
    for index, elem in enumerate(nums):
        if elem % 2 == 0:
            new_arr.append(index)
    return new_arr


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     17.2 MiB     17.2 MiB           1   @profile
    23                                         def func_1(nums):
    24     17.2 MiB      0.0 MiB           1       new_arr = []
    25     17.5 MiB      0.3 MiB           1       x = list(range(10000))
    26     17.8 MiB      0.3 MiB           1       zn = list(range(10000))
    27     17.8 MiB      0.0 MiB         101       for i in range(len(nums)):
    28     17.8 MiB      0.0 MiB         100           if nums[i] % 2 == 0:
    29     17.8 MiB      0.0 MiB          50               new_arr.append(i)
    30     17.8 MiB      0.0 MiB           1       return new_arr


Filename: /home/kmoscow/geekbrains_python/geekbrains_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     17.8 MiB     17.8 MiB           1   @profile()
    34                                         def func_2(nums):
    35     17.8 MiB      0.0 MiB           1       new_arr = []
    36     17.8 MiB      0.0 MiB           1       cx = list(range(10000))
    37     17.8 MiB      0.0 MiB           1       czn = list(range(10000))
    38     17.8 MiB      0.0 MiB         101       for index, elem in enumerate(nums):
    39     17.8 MiB      0.0 MiB         100           if elem % 2 == 0:
    40     17.8 MiB      0.0 MiB          50               new_arr.append(index)
    41     17.8 MiB      0.0 MiB           1       return new_arr


Filename: /home/kmoscow/geekbrains_python/geekbrains_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     17.8 MiB     17.8 MiB           1   @profile()
    45                                         def func_3(nums):
    46     17.8 MiB      0.0 MiB           1       new_arr = []
    47     18.0 MiB      0.3 MiB           1       cx1 = list(range(20000))
    48     18.5 MiB      0.5 MiB           1       czn1 = list(range(20000))
    49     18.5 MiB      0.0 MiB         101       for index, elem in enumerate(nums):
    50     18.5 MiB      0.0 MiB         100           if elem % 2 == 0:
    51     18.5 MiB      0.0 MiB          50               new_arr.append(index)
    52     18.5 MiB      0.0 MiB           1       return new_arr


Filename: /home/kmoscow/geekbrains_python/geekbrains_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    55     18.0 MiB     18.0 MiB           1   @profile()
    56                                         def func_4(nums):
    57     18.0 MiB      0.0 MiB           1       new_arr = []
    58     18.0 MiB      0.0 MiB           1       cx2 = list(range(20000))
    59     18.5 MiB      0.5 MiB           1       czn2 = list(range(20000))
    60     18.5 MiB      0.0 MiB         101       for index, elem in enumerate(nums):
    61     18.5 MiB      0.0 MiB         100           if elem % 2 == 0:
    62     18.5 MiB      0.0 MiB          50               new_arr.append(index)
    63     18.5 MiB      0.0 MiB           1       return new_arr



Process finished with exit code 0
"""

# Вывод: пробовал разные функции из предыдущих заданий, но оказалось что они потребляют очень мало памяти, поэтому решил
# "утяжелить" функции при помощи list(range(x)), но так и не понял как работает память. Загадкой для меня оказалось
# почему list(range(10000)) употребляет только в 1 функции, а во второй - память не выделяется. Но когда использовал
# list(range(20000)), в 3-ей ф-ции два раза выделялась память, а в 4-ой фунции - только один раз. Для меня осталось
# загадкой как выделяется память для этого процесса (предсказать я не смог)
# P.S. Не уверен что правильно понял и справился с поставленной задачей
# (venv) kmoscow@kali:~/geekbrains_python/geekbrains_python$ python --version
# Python 3.8.6
# Разрядность ('64bit', 'ELF')

if __name__ == '__main__':
    func_1(n)
    func_2(n)
    func_3(n)
    func_4(n)
    print(platform.architecture())
