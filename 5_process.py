# https://www.coursera.org/learn/diving-in-python/lecture/WfkO5/protsiess-i-iegho-kharaktieristiki

import time
import os

# Получаем ID запущенного процесса
pid = os.getpid()

while True:
    print(pid, time.time())
    time.sleep(2)
