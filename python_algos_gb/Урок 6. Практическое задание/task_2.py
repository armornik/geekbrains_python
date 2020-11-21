"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
import shelve
from memory_profiler import profile


@profile()
def game_memory_1():
    with shelve.open("my_file1", flag="c", writeback=False) as file:
        for num in range(100):
            file[str(num)] = num
        print(file)
        for num in range(200):
            file[str(num)] = num
        print(file)


@profile()
def game_memory_2():
    with shelve.open("my_file2", flag="c", writeback=True) as file:
        for num in range(100):
            file[str(num)] = num
        print(file)
        for num in range(200):
            file[str(num)] = num
        print(file)


if __name__ == "__main__":
    game_memory_1()
    game_memory_2()


"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     17.3 MiB     17.3 MiB           1   @profile()
    13                                         def game_memory_1():
    14     17.9 MiB      0.7 MiB           1       with shelve.open("my_file1", flag="c", writeback=False) as file:
    15     18.2 MiB      0.0 MiB         101           for num in range(100):
    16     18.2 MiB      0.3 MiB         100               file[str(num)] = num
    17     18.4 MiB      0.0 MiB         201           for num in range(200):
    18     18.4 MiB      0.2 MiB         200               file[str(num)] = num


Filename: /home/kmoscow/geekbrains_python/geekbrains_python/python_algos_gb/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     18.4 MiB     18.4 MiB           1   @profile()
    22                                         def game_memory_2():
    23     18.4 MiB      0.0 MiB           1       with shelve.open("my_file2", flag="c", writeback=True) as file:
    24     18.4 MiB      0.0 MiB         101           for num in range(100):
    25     18.4 MiB      0.0 MiB         100               file[str(num)] = num
    26     18.4 MiB      0.0 MiB         201           for num in range(200):
    27     18.4 MiB      0.0 MiB         200               file[str(num)] = num



Process finished with exit code 0"""

# Вывод: При выполнении первой функции с атрибутом writeback=False, проходя по циклу increment и Memusage -увеличивается
# При выполнении второй функции с атрибутом writeback=True - этого не происходит.
# P.S. При большом значении range(20000) - память себя ведёт по другому/

# Для работы с бинарными файлами в Python может применяться модуль - shelve. Он сохраняет объекты в файл с
# определенным ключом. Затем по этому ключу может извлечь ранее сохраненный объект из файла. Процесс работы с данными
# через модуль shelve напоминает работу со словарями, которые также используют ключи для сохранения
# и извлечения объектов.
