dict_number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open('5_4_1.txt', 'r') as f:
        with open('5_4_2.txt', 'w') as f_rus:
            for line in f:
                english_meaning, number = line.split(' - ')
                if english_meaning in dict_number:
                    f_rus.write(f'{dict_number[english_meaning]} - {number}')
except IOError:
    print('Ошибка ввода-вывода')
