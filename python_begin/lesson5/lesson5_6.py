try:
    with open('5_6.txt', 'r') as f:
        my_dict = {}
        for line in f:
            subject, info_subject = line.split(':')
            hour = 0
            for string in info_subject.split():
                for number in string.split('('):
                    try:
                        number = int(number)
                    except ValueError:
                        pass
                    else:
                        hour += number
            my_dict[subject] = hour
        print(my_dict)
except IOError:
    print('Ошибка ввода-вывода')
