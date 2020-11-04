data_user = list(input('Введите значения элементов списка через пробел: ').split())
len_data_user: int = len(data_user)
if len_data_user < 2:
    print('Список должен содержать не менее 2-ух элементов')
elif len_data_user % 2 == 0:
    print(f'Списко до изменения: {data_user}')
    for i in range(len_data_user):
        if i % 2 == 0:
            data_user[i + 1], data_user[i] = data_user[i], data_user[i + 1]
    print(f'Списко после изменения: {data_user}')
else:
    print(f'Списко до изменения: {data_user}')
    for i in range(len_data_user-1):
        if i % 2 == 0:
            data_user[i + 1], data_user[i] = data_user[i], data_user[i + 1]
    print(f'Списко после изменения: {data_user}')

