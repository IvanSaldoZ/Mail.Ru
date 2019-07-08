# https://www.coursera.org/learn/diving-in-python/lecture/CXVes/kontiekstnyie-mieniedzhiery
# Контекстный менеджер
class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


with open_file('test.log', "w") as f:
    f.write("inside 'open file' context manager")

with open_file('test.log', "r") as f:
    print(f.read())


# ----------------------------------------------
# Таймер с использованием контекстного менеджера (для подсчета времени выполнения алгоритма может использоваться)
import time

class timer:
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self  # Возвращает себя, когда используется оператор "as" (см. далее)

    def __exit__(self, *args):
        print("Elapsed: {}".format(self.current_time()))

with timer() as t:
    time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    time.sleep(1)


