from sys import argv

script_name, elaboration, bet, award = argv
try:
    elaboration = float(elaboration)
    bet = float(bet)
    award = float(award)
except ValueError:
    print('Параметры должны быть числами')


def salary(elaboration: float, bet: float, award: float):
    return print(f'Заработная плата сотрудника составляет: {elaboration * bet + award}')


salary(elaboration, bet, award)
