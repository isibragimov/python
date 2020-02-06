import os
import sys
import shutil
import psutil
import random


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False


def sys_info():
    print("Информация о системе:")
    print("Имя текущей директории:", os.getcwd())
    print("Платформа OS:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Логин пользователя:", os.getlogin())
    print("Количество CPU:", os.cpu_count())


def remove_dupl(filename):
    if filename.endswith('.dupl'):
        os.remove(filename)
    if not os.path.exists(filename):
        return True


def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1


def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print("Файл", fullname, " был случайно удален")


def main():
    print("MyPython")
    print("Привет!")
    name = input("Ваше имя: ")
    print("Привет, ", name)

    answer = ''

    while answer != 'q':
        answer = input("Давайте поработаем? (Y/N/q) ")
        if (answer == 'Y') or (answer == 'y'):
            print("Я умею:")
            print(" [1] - выведу список файлов")
            print(" [2] - выведу информацию о системе")
            print(" [3] - выведу список процессов")
            print(" [4] - продублирую файлы в текущей директории")
            print(" [5] - продублирую файл который укажет пользователь")
            print(" [6] - удаляю файлы с окончанием .dupl в директории, которую укажет пользователь")
            print(" [7] - удалю случайный файл")

            action = input("Выберите действие: ")

            if action == '1':
                print(os.listdir())


            elif action == '2':
                sys_info()


            elif action == '3':
                print(psutil.pids())


            elif action == '4':
                print("Дублирование файлов в текущей директории")
                duble_files('.')


            elif action == '5':
                print("Дублирование указанного файла")
                user_file = input("Укажите имя файла для дублирования: ")
                duplicate_file(user_file)


            elif action == '6':
                print("Удаление файлов с окончанием .dupl в директории, которую укажет пользователь")
                remove_dupl_col = 0
                user_dir = input("Укажите путь директории для удаления .dupl: ")
                file_list = os.listdir(user_dir)
                for f in file_list:
                    full_path = os.path.join(user_dir, f)
                    if remove_dupl(full_path):
                        remove_dupl_col += 1
                print("Дублей удалено: ", remove_dupl_col)


            elif action == '7':
                print("Удаление случайного файла")
                dirname = input("Укажите имя директории: ")
                random_delete(dirname)


            else:
                print("Неизвестный ответ")

        elif (answer == 'N') or (answer == 'q'):
            print("До свидания!")
        else:
            print("Неизвестный ответ")


if __name__ == "__main__":
    main()
