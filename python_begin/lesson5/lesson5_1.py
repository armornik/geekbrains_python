try:
    with open('new_file.txt', 'w') as f:
        while True:
            text = input('Введите текст, необходимый записать в файл: ')
            if text == '':
                break
            else:
                f.write(text+'\n')
except IOError:
    print('Ошибка ввода-вывода')
