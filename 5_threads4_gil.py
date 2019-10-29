# https://www.coursera.org/learn/diving-in-python/lecture/BRtbx/global-naia-blokirovka-intierprietatora
# Многопоточность на блокировках, синхронизация потоков

from threading import Thread

import time

def count(n):
    while n > 0:
        n -= 1

# series run
t0 = time.time()

num = 100_000_000
count(num)
count(num)
print(time.time() - t0)

#parallel run
t0 = time.time()
th1 = Thread(target=count, args=(num,))
th2 = Thread(target=count, args=(num,))

th1.start()
th2.start()

th1.join()
th2.join()

print(time.time() - t0)

# В итоге задача cpu_bound (т.е. задача, требующая вычислительных ресурсов CPU) будет работать ДОЛЬШЕ, чем
# последовательная (захватывается Gil - Global Interpretator Lock).
# Быстрее получается только в случае операций ввода-вывода (все системные вызовы) (потому что там gil не захватывается)
