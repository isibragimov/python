while True:
    Num = int(input("Введите число от 0 до 10: "))
    if Num >= 0 and Num <=10:
        print("Ваше число в квадрате:", Num ** 2)
        break
    else:
        print("Не верно! Введите число от 0 до 10: ", Num)
