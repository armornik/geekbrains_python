first_result: int = 0
required_result: int = 0
while True:
    if first_result < required_result:
        required_number_of_days: int = 1
        while first_result < required_result:
            first_result *= 1.1
            required_number_of_days += 1
        break
    else:
        first_result: int = int(input('Введите результат первого дня: '))
        required_result: int = int(input('Введите требуемый результат: '))
    if first_result >= required_result:
        print('Требуемый результат должен быть больше результата первого дня')
print(f'На {required_number_of_days}-й день спортсмен достиг результата - не менее {required_result} км.')
