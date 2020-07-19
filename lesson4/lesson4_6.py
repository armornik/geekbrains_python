from itertools import count, cycle

user_input: str = input('Введите число до 100: ')

try:
    if int(user_input) >= 100:
        print('Вводимое число должно быть меньше 100')
    else:
        for el in count(int(user_input)):
            if el > 100:
                break
            else:
                print(el)
except ValueError:
    print('Необходимо ввести число')
print(f'А теперь слово "Стоп" будет повторено {int(user_input)} раз')
с = 0
for el in cycle(['Стоп']):
    if с > int(user_input):
        break
    print(el)
    с += 1
