#Семейная пара собирается в отпуск
#СКаждый из супругов собирает в поездку вещи
#Max взял эти вещи
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
#Kate взяла эти вещи
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# Какие вещи взяли супруги
print(max_things | kate_things)
# Найти вещи повторяются
print(max_things & kate_things)
# Какие вещи не взял max, но взял kate
print(max_things - kate_things)
# Какие вещи не взяла kate, но взял max
print(kate_things - max_things)