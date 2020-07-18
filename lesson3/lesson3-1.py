def division(var_1, var_2):
    if ord(str(var_2)) == 48:
        return 'Деление на 0 недопустимо, бесконечность....'
    return var_1 / var_2


print(division(9, 3))
print(division(9, 6))
print(division(10, 0))

