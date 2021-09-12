import socket

import settings


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((settings.IP, settings.PORT))

while True:
    message = input('You: ')
    if not message:
        break
    try:
        client_socket.send(message.encode())
    except socket.error:
        break
    
client_socket.close()
    