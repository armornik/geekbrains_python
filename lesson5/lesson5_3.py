try:
    with open('salary5_3.txt', 'r') as f:
        n_string = 0
        salary_sum = 0
        staff_small_salary = []
        for line in f:
            staff, salary = line.split()
            salary = int(salary)
            if salary < 20000:
                staff_small_salary.append(staff)
            salary_sum += salary
            n_string += 1
        print(f'Следующие сотрудники имеют з/п менее 20к: {", ".join(staff_small_salary)}')
        print(f'Средняя з/п на предприятии составляет: {salary_sum / n_string:.2f}')
except IOError:
    print('Ошибка ввода-вывода')
