import socket
# сокет содержит тип соединения, передача потокол -по умолчаниб TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
# тип socket.socket
# fileno - возвращает тип и протокол сокета
server.bind(('127.0.0.1', 53210))

server.listen(10)# количество ссоединений  в очереде
while True:
    client_sock, client_addr = server.accept()
    # можно подключиться через telnet '127.0.0.1', 53210
    print('Connected by',  client_addr)

    while True:
        data = client_sock.recv(1024)
        print(data)
        if not data:
            break
            client_sock.sendall(data)
        client_sock.close()

# micromind.me/posts/writing-python-web-server-part-1
