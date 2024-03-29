# https://www.coursera.org/learn/diving-in-python/lecture/XK72a/taimauty-i-obrabotka-sietievykh-oshibok
# создание сокета, таймауты и обработка ошибок
# сервер

import socket

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        conn.settimeout(5)  # timeout := None|0|gt 0
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break

                if not data:
                    break
                print(data.decode("utf8"))



