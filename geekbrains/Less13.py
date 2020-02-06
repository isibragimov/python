import random

start = 1
end = 100

print('Игра угадай число от 1 до 100!')
print('------------------------------')
print('Загадай число от 1 до 100')

while True:
    number = random.randint(start, end)
    print(f'Вы загадали: {number}?')
    answer = input('Варианты ответа (Если число меньше введите "<" больше ">" угадал "=" ')
    if answer == '<':
            end = number - 1
    elif answer == '>':
            start = number + 1

    elif answer == '=':
        break

print('Ура я выиграл!')