data_user: list = input('Введите стоку: ').split()
for num, word in enumerate(data_user):
    if len(word) > 10:
        print(num, word[:10])
    else:
        print(num, word)
