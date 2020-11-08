"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
from hashlib import sha256


def len_substring(test_str):
    substring = set([test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)])
    res = [sha256(sub.encode()).hexdigest() for sub in substring if sub != test_str]
    return len(res)


a = len_substring('papa')
print(a)
