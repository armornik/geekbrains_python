revenue: int = int(input('Введите выручку: '))
cost: int = int(input('Введите издержку: '))
if revenue - cost < 0:
    print('Фирма сработала в убыток')
elif revenue - cost == 0:
    print('Идеальный баланс (делить всё равно нечего)')
else:
    profit = (revenue - cost)
    profitability: float = profit / revenue
    print(f'Ура, мы получили прибыль. Рентабельность прибыли составляет: {profitability:.2f}')
    number_of_employees: int = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / number_of_employees
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет: {profit_per_employee:.2f} рублей на человека')
