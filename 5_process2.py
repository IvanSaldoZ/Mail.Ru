# https://www.coursera.org/learn/diving-in-python/lecture/14PPx/sozdaniie-protsiessov



# -------------------- ТОЛЬКО ДЛЯ LINUX
import time
import os

pid = os.fork()
if pid == 0:
    # дочерний процесс
    while True:
        print('child:', os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("parent:", os.getpid())
    os.wait()

# --------------------

# --------------------------

from multiprocessing import Process

def f(name):
    print("Hello", name)

p = Process(target=f, args=("Bob", ))
p.start()
p.join()