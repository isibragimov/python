from os import path, getcwd, mkdir, rmdir
from random import choice


def make_dir():
    for i in range(1, 10):
        new_path = path.join(getcwd(), '{}_{}'.format('dir', i))
        mkdir(new_path)


def remove_dir():
    for i in range(1, 10):
        new_path = path.join(getcwd(), '{}_{}'.format('dir', i))
        rmdir(new_path)


def random_element(my_list):
    if my_list:
        result = choice(my_list)
        return result