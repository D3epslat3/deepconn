import eventQueue
from eventQueue import evQueue

import user
from user import users

def handle_message(message):
    response = None

    sender = message[0]
    event = message[1]

    if event == 'connection':
        res = users.add(sender)
        if not res:
            response = 'User already exists'
        response = 'User connected as %s' % message[1]

    if event == 'disconnection':
        users.remove(sender.username)
        response = None

    if event == 'message':
        receiver = users.get(message[2])
        if receiver.notify(sender.username, message[3]):
            response = 'Message broken'
        response = 'Message sent'

    response = f'{response}\n'
    print('responding %s' % response)
    sender.socket.sendall(response.encode())

def handle_messages():
    while True:
        if evQueue.is_empty():
            continue
        
        message = evQueue.get()

        handle_message(message)
