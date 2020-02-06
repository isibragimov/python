print("MyPython")
print("Привет!")
name = input("Ваше имя: ")
print("Привет, ", name)
answer = input("Давайте поработаем? (Y/N)")

if answer == 'Y':
	action = input("Выберите действие: 1. Читать 2. Писать 3. Рисовать: ")
	if action == '1':
		print("Отличный выбор, у нас много книг!")
	elif action == '2':
		print("Ваш текст интересный!")
	elif action == '3':			
		print("Красивый рисунок!")
	else:
		print("Неизвестный ответ")			
elif answer == 'N':
	print("До свидания!")
else:
	print("Неизвестный ответ")
	