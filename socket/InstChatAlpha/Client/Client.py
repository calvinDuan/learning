import socket
import threading
from Utils.Tags import Pointer
from Utils.Tools import msg_format

class MyClient:
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = Pointer.HOST_CLIENT
        self._port = Pointer.PORT
        self._header_size = Pointer.HEADER_SIZE
        self._format = Pointer.FORMAT
        self._disconnected = Pointer.DISCONNECT_MSG
        self._is_ended = False

    def client_start(self):
        self._client.connect((self._host, self._port))
        thread_recv = threading.Thread(target= self._receive)
        thread_recv.setDaemon(True)
        thread_recv.start()
        while not self._is_ended:
            msg = input()
            self._send(msg)

    def _send(self, msg: str):
        buffered_msg = f'{len(msg):<{self._header_size}}' + msg
        self._client.send(buffered_msg.encode(self._format))
        if msg == self._disconnected:
            self._is_ended = True

    def _receive(self):
        while True:
            msg_len = self._client.recv(self._header_size).decode(self._format)
            if msg_len:
                msg_length = int(msg_len)
                msg = self._client.recv(msg_length).decode(self._format)
                output = msg_format(msg)
                print(output)


