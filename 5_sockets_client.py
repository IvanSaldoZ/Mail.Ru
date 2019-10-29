# https://www.coursera.org/learn/diving-in-python/lecture/3YYVH/sokiety-kliient-siervier
# создание сокета, клиентская часть

import socket


# sock = socket.socket()
# sock.connect(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()


# Или более короткая запись

sock = socket.create_connection(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf8"))
sock.close()


# ---------------------------
# Но лучше делать через Контекстный менеджер, потому что он автоматически закрывает соединение, как отработает

with socket.create_connection(("127.0.0.1", 10001)) as sock:
    sock.sendall("ping".encode("utf8"))