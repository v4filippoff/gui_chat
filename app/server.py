import threading
import socket

import settings


class ClientConnectionThread(threading.Thread):
    """
    Поток, выделенный под одного клиента
    """
    def __init__(self, client_socket, client_addr):
        super().__init__(self)
        self.client_socket = client_socket
        self.client_addr = client_addr

    def run(self):
        try:
            while True:
                data = self.client_sock.recv(1024)
                if not data:
                    break
                print(data.decode())
        except socket.error:
            pass
        finally:
            print('Disconnected', self.client_addr)
            self.client_socket.close()


class Server:
    """
    Сервер, который прослушивает порт и принимает подключения от клиентов
    """
    def __init__(self, port=55000):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', port))
        self.server_socket.listen()

    def run(self):
        while True:
            client_socket, client_addr = self.accept_connection()
            self.create_new_thread(client_socket, client_addr)

    def accept_connection(self):
        client_socket, client_addr = self.server_socket.accept()
        print(f'Connected ({client_addr})')
        return client_socket, client_addr

    def create_new_thread(self, client_socket, client_addr):
        client_connection = ClientConnectionThread(client_socket, client_addr)
        client_connection.start()


if __name__ == '__main__':
    server = Server(port=settings.PORT)
    server.run()


