import user as userlib
from eventQueue import evQueue
def handle_client(client_socket):
    client_name = client_socket.recv(1024).decode().strip()
    user = userlib.User(client_name, client_socket)

    evQueue.put((user, 'connection'))

    while True:
        message = client_socket.recv(1024).decode().strip()

        if message == 'exit':
            break

        evQueue.put((user, 'message', message))
    
    evQueue.put(('disconnection', user))
    client_socket.close()
