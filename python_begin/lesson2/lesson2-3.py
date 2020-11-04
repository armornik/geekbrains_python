input_month: str = input('Введите номер месяца (от 1 до 12): ')
dict_month: dict = {'1': 'Winter (Зима)', '2': 'Winter (Зима)', '3': 'Spring (Весна)', '4': 'Spring (Весна)', \
                    '5': 'Spring (Весна)', '6': 'Summer (Лето)', '8': 'Summer (Лето)', '9': 'Autumn (Осень)', \
                    '10': 'Autumn (Осень)', '11': 'Autumn (Осень)', '12': 'Winter (Зима)', }
list_month: list = [['12', '1', '2', 'Winter (Зима)'], ['3', '4', '5', 'Spring (Весна)'], \
                    ['6', '7', '8', 'Summer (Лето)'], ['9', '10', '11', 'Autumn (Осень)']]
if input_month not in dict_month:
    print('Вы неверно ввели месяц (необходимо ввести число от 1 до 12)')
else:
    print('Решение при помощи словаря:')
    print(f'Введённый Вами месяц {input_month} - ремя года: {dict_month[input_month]}')
for i in list_month:
    for j in i:
        if input_month == j:
            print('Решение при помощи списка:')
            print(f'Введённый Вами месяц {input_month} - ремя года: {i[3]}')
