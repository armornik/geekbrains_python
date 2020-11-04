try:
    with open('new_file.txt', 'r') as f:
        n_string = 0
        n_word = 0
        for number_line, line in enumerate(f, start=1):
            print(f'В строке {number_line} {len(line.split())} слов')
            n_string += 1
        print(f'В файле всего {n_string} строки.')
except IOError:
    print('Ошибка ввода-вывода')
