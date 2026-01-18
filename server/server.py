import socket
import threading

import eventQueue
from eventQueue import evQueue

import eventListener
from eventListener import handle_messages

import user
from user import users

import client
from client import handle_client

PORT = 8080

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))

    print('Server started on %s:%d' % (socket.gethostbyname(socket.gethostname()), PORT))

    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

    server_socket.close()

if __name__ == '__main__':
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=handle_messages, daemon=True).start()

    while True:
        try:
            inmsg = input()
            if inmsg == 'exit':
                break
            if inmsg == 'users':
                print(users.users)
        except KeyboardInterrupt:
            break
