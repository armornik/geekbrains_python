second_from_user: int = int(input('Введите количество секунд: '))
hours: int = second_from_user // 3600
minutes: int = (second_from_user - hours * 3600) // 60
seconds: int = second_from_user - hours * 3600 - minutes * 60
if hours < 10:
    hours: str = '0' + str(hours)
if minutes < 10:
    minutes: str = '0' + str(minutes)
if seconds < 10:
    seconds: str = '0' + str(seconds)
print(f'Введённые секунды составляют: {hours}:{minutes}:{seconds}')
