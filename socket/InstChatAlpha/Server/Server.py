import socket
import threading
from Utils.Tags import Pointer
from Utils.Tools import msg_format


class ChatServer:
    def __init__(self):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = Pointer.HOST
        self._port = Pointer.PORT
        self._header_size = Pointer.HEADER_SIZE
        self._format = Pointer.FORMAT
        self._disconnected = Pointer.DISCONNECT_MSG
        self._conn_dict = dict()
        self._is_ended = False
        self._label = 0
        self._getting_client = False
        self._new_conn = False
        self._is_sending = False
        self._server.bind((self._host, self._port))

    def _get_client(self):
        while True:
            self.conn, addr = self._server.accept()
            self._conn_dict[self._label] = self.conn
            self._new_conn = True

    def _receive_client(self, conn: socket.socket, label: int):
        connected = True
        while connected:
            msg_len = conn.recv(self._header_size).decode(self._format)
            msg_length = int(msg_len)
            msg = conn.recv(msg_length).decode(self._format)
            if msg == self._disconnected:
                connected = False
                del self._conn_dict[label]
            output = msg_format(msg)
            print(output)

        conn.close()

    def _send_client(self):
        while True:
            msg = input()
            buffered_msg = f'{len(msg):<{self._header_size}}' + msg
            for label, conn in self._conn_dict.items():
                conn.send(buffered_msg.encode(self._format))
            if msg == self._disconnected:
                if threading.active_count() - 3 != 0:
                    print('Active Users Online, Can Not Terminate')
                else:
                    print('ending')
                    self._is_ended = True

    def server_start(self):
        self._server.listen()
        while not self._is_ended:
            if not self._getting_client:
                thread_client = threading.Thread(target=self._get_client)
                self._getting_client = True
                thread_client.setDaemon(True)
                thread_client.start()
            if self._new_conn:
                thread_recv = threading.Thread(target=self._receive_client, args=[self.conn, self._label])
                self._label += 1
                self._new_conn = False
                thread_recv.start()
            if not self._is_sending:
                thread_send = threading.Thread(target=self._send_client)
                thread_send.setDaemon(True)
                thread_send.start()
                self._is_sending = True




