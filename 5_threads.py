# https://www.coursera.org/learn/diving-in-python/lecture/Ff3fP/sozdaniie-potokov

# Создание отдельного оптока
from threading import Thread

def f(name):
    print("hello", name)

th = Thread(target=f, args=("Bob",))
th.start()
th.join()



# Альтернативный метод создания потока
class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        '''Метод run уже выполняется в отдельном потоке'''
        print("hello", self.name)

th = PrintThread("Mike")  # Инициализация потока
th.start()  # Запуск потока
th.join()   # Завершение потока (освобождение памяти)



# -------------------------------
# Распределение цикла по потокам
# Пул потоков, concurrent.futures.Future - это такой объект, который еще выполняется и завершится в будущем

from concurrent.futures import ThreadPoolExecutor, as_completed

def f(a):
    return a*a

# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
