# https://www.coursera.org/learn/diving-in-python/lecture/Xifvg/sinkhronizatsiia-potokov
# Многопоточность на очередях

from queue import Queue
from threading import Thread

def worker(q, n):
    while True:
        item = q.get()
        if item is None:
            break
        print("process data:", n, item)

# Инициируем 5 очередей
q = Queue(5)


# Передаем в поток нашу функцию с аргементами - объект очереди и номер потока
th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
# Запускаем потоки и ждем (цикл-то в worker-е бесконечный)
th1.start()
th2.start()

# Так, теперь добавляем в очередь 50 элементов
for i in range(50):
    q.put(i)

q.put(None)
q.put(None)

# Завершаем потоки
th1.join()
th2.join()
