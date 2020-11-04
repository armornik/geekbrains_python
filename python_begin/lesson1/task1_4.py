# Задача 4
int_from_user: str = input('Введите число: ')
int_max = ''
for digit in int_from_user:
    if digit > int_max:
        int_max = digit
print(f'Самая большая цифра в числе: {int_max}')
