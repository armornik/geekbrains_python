def fact(user_input):
    a = 1
    for i in range(1, user_input + 1):
        a *= i
        yield a


user_input: str = input('Введите число: ')

try:
    user_input: int = int(user_input)
except ValueError:
    print('Необходимо ввести число')

for x in fact(user_input):
    print(x)
