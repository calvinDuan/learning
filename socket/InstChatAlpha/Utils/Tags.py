import socket


class Pointer:
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    HEADER_SIZE = 10
    FORMAT = 'utf-8'
    DISCONNECT_MSG = 'bye'
    HOST_CLIENT = '192.168.50.202'
