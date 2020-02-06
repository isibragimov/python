Name = input("Введите ваше имя: ")
Surname = input("Введите вашу фамилию: ")
Age = int(input("Введите ваш возраст: "))
Weight = int(input("Введите ваш вес: "))

if Age <= 30 and Weight >= 50 and Weight <= 120:
    print("Пациент:", Name, Surname, Age, "год,", "вес", Weight, "- хорошее состояние")
elif Age > 30 and Age <= 40 and Weight <= 50 or Weight >= 120:
    print("Пациент:", Name, Surname, Age, "год,", "вес", Weight, "- следует заняться собой")
elif Age > 40 and Weight <= 50 or Weight >= 120:
    print("Пациент:", Name, Surname, Age, "год,", "вес", Weight, "- следует обратится к врачу!")
