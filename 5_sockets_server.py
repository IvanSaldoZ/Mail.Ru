# https://www.coursera.org/learn/diving-in-python/lecture/3YYVH/sokiety-kliient-siervier
# создание сокета, серверная часть

import socket

# https://docs.python.org/3/library/socket.html
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))  # max port 65535
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    # process data
    print(data.decode("utf8"))

conn.close()
sock.close()

# ---------------------------
# Но лучше делать через Контекстный менеджер, потому что он автоматически закрывает соединение, как отработает

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))



