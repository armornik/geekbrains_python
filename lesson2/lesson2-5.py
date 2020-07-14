source_set: list = [10, 8, 7, 6, 3, 3, 1, ]
print('Исходный список', source_set)
# Для проверки места "вставки" элемента необходимо поменять тип преобразования на float
data_user: int = int(input('Введите число: '))
if data_user <= source_set[-1]:
    source_set.append(data_user)
else:
    for i in range(len(source_set)):
        if data_user > source_set[i]:
            source_set.insert(i, data_user)
            break
print('Изменённыё список', source_set)
