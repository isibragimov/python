def attack(damage, enemy):
    enemy['health'] = enemy['health'] - damage
    return damage

def defence(damagе, armor):
    damagе = damagе / armor
    return int(damagе)


player = { 'name' : '',
           'health' : 100,
           'damage' : 50,
           'armor' : 3 }

enemy = { 'name' : 'Ork',
          'health' : 200,
          'damage' : 25,
          'armor' : 3 }

player['name'] = input('Введите имя: ')


while player['health'] > 0:
    damage_player = attack(defence(player['damage'], enemy['armor']), enemy)
    if enemy['health'] <= 0:
        print('Игрок {} нанес урон {}. У {} осталось {} здровья. Победа!!!'.format(player['name'], damage_player, enemy['name'], enemy['health']))
        break
    print('Игрок {} нанес урон {}. У {} осталось {} здровья.'.format(player['name'], damage_player, enemy['name'], enemy['health']))

    damage_enemy = attack(defence(enemy['damage'], player['armor']), player)
    if player['health'] <= 0:
        print('Игрок {} нанес урон {}. У {} осталось {} здровья. Вы проиграли!!!'.format(enemy['name'], damage_enemy, player['name'], player['health']))
        break

    print('Игрок {} нанес урон {}. У {} осталось {} здровья.'.format(enemy['name'], damage_enemy, player['name'], player['health']))




# def data(name, age, city):
#     return '{}, {} год(а), проживает в городе {}'.format(name, age, city)
#
# questions = ['имя', 'возраст', 'город']
# answer = []
#
# for question in questions:
#     answer.append(input('Введите {} '.format(question)))
#
# print(data(answer[0], answer[1], answer[2]))


# def max_number(numbers):
#     return 'Максимальное число {}'.format(max(numbers))

# numbers = []
#
# for i in range(3):
#     numbers.append(int(input('Введите {} число: '.format(i + 1))))
#
# print(max_number(numbers))