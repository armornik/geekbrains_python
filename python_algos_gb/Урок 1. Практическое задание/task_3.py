"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

# Вариант 1
from collections import OrderedDict

economics = {'MMM': 10000, 'Sber': 100000, 'Audi': 50000, 'BMW': 75000, 'UAZ': 30000}

# Наибольшая сложность O(n)
result = [] # O(1)
my_economics = OrderedDict(sorted(economics.items(), key=lambda x: x[1])) # O(nLog(n))
for _ in range(3): # O(n)
    result.append(my_economics.popitem(last=True)) # O(1) и popitem и append

print(result)

# Вариант 2

economics = {'MMM': 10000, 'Sber': 100000, 'Audi': 50000, 'BMW': 75000, 'UAZ': 30000}

# O(nLog(n))
result2 = list(sorted(economics.items(), key=lambda x: x[1], reverse=True))[:3] # list - O(5), sorted - O(nLog(n)), срез - O(3)
print(result2)

# Второе решение эффективнее
