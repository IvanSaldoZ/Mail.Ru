# D:\Info\Python\Курс по Python-у на Coursera\Курс 1. Погружение в Питон\Week 1\3. Организация кода и окружение

import this
import inspect
import os

# Получаем директорию, в которой находится модуль:
dir_name = inspect.getfile(this)
print(dir_name)
print(dir(dir_name))
modules_list = os.listdir("D:/Codes/Programming/Python_3.7.3/lib/")
print(modules_list)
