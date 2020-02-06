cities = {'Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow'}

print(cities)
cities.add('Burma')
print(cities)
cities.add('Moscow')
print(cities)
cities.remove('Moscow')
print(cities)
print(len(cities))
print('Paris' in cities)

for city in cities:
    print(city)