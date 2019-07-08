# https://www.coursera.org/learn/diving-in-python/lecture/wIo7L/klassy-iskliuchienii-i-ikh-obrabotka
# https://www.coursera.org/learn/diving-in-python/lecture/oF2h7/gienieratsiia-iskliuchienii
# Исключения


#print(1/0)


# -----------------------
class MyClass:
    pass


obj = MyClass()
# obj.foo # AttributeError: 'MyClass' object has no attribute 'foo'


# -----------------------

l = [1,2]
# l[10]  # IndexError: list index out of range


# -----------------------
# int("afadf")  # ValueError: invalid literal for int() with base 10: 'afadf'


# -----------------------
# 1 + "10"  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    1 / 0
except Exception:
    print("Ошибка: нельзя делить на ноль")


# Не в общем исключения лучше НЕ обрабатывать, а разделять по типам
# НЕВЕРНО, НЕ БУДЕТ ОБРАБАТЫВАТЬ Ctrl+C
while True:
    try:
        raw = input("Введите число: ")
        number = int(raw)
        break
    except:
        print("Некорректное значение")

# Поэтому лучше конкретно указывать, в чем дело
while True:
    try:
        raw = input("Введите число (верно): ")
        number = int(raw)
        break
    except ValueError:
        print("Некорректное значение")
    except KeyboardInterrupt:
        print("Выход")
        break

# --------------------

f = open("/etc/hosts")
try:
    for line in f:
        print(line.rstrip("\n"))
        1 / 0
        # f.close()
except OSError as err:
    print("Ошибка доступа к файлу", err.errno, err.strerror)
finally:
    f.close()  # Блок finally выполняется всегда, независимо от того, произошло исключение или нет

# --------------------


# Инструкция assert

assert True