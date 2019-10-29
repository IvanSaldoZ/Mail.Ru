# https://www.coursera.org/learn/diving-in-python/lecture/Xifvg/sinkhronizatsiia-potokov
# Многопоточность на блокировках, синхронизация потоков

import threading

class Point(object):
    def __init__(self):
        self._mutex = threading.RLock()  # Записываем объект блокировки, чтобы потом с ним работать
        self._x = 0
        self._y = 0

    def get(self):
        # Включаем блокировку на получение (чтобы не получить сначала x, а потом y, а получать ТОЛЬКО ВМЕСТЕ)
        # Типа транзакции для SQL
        with self._mutex:
            return (self._x, self._y)

    def set(self, x, y):
        # Блокировка (чтобы не задавалось сначала x, потом y, а ТОЛЬКО ВМЕСТЕ)
        # Типа транзакции для SQL
        with self._mutex:
            self._x = x
            self._y = y



# Без контекстного менеджера:

a = threading.RLock()
b = threading.RLock()

def foo():
    try:
        a.acquire()  # Захватить блокировку на a
        b.acquire()
    finally:
        a.release()  # Освободить блокировку на a
        b.release()