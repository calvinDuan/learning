import socket
import threading
from Tools.Config import Standard


class ChatServer:
    def __init__(self):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((Standard.HOST, Standard.PORT))
        self._server.listen()

        self._client_dict = dict()
        self.terminate = False

    def _broadcast(self, msg: str):
        buffered_msg = f'{len(msg):<{Standard.HEADER_SIZE}}' + msg
        for name, client in self._client_dict.items():
            client.send(buffered_msg.encode(Standard.FORMAT))

    def _handle(self, name: str, client: socket.socket):
        print('handling')
        while True:
            try:
                msg_len = int(client.recv(Standard.HEADER_SIZE).decode(Standard.FORMAT))
                msg = client.recv(msg_len).decode(Standard.FORMAT)
                msg = f'{name}:\n{msg}'
                self._broadcast(msg)
            except:
                del self._client_dict[name]
                msg = f'{name} left the chat'
                client.close()
                self._broadcast(msg)
                break

    def _connect(self):
        while True:
            conn, addr = self._server.accept()
            thread = threading.Thread(target=self._initialize, args=[conn])
            thread.start()

    def _initialize(self, conn: socket.socket):
        instruction = 'Please enter your user name'
        buffered_instruction = f'{len(instruction):<{Standard.HEADER_SIZE}}' + instruction
        conn.send(buffered_instruction.encode(Standard.FORMAT))
        name = conn.recv(1024).decode(Standard.FORMAT)
        if name in self._client_dict:
            name = name + ' '
        self._client_dict[name] = conn
        msg = f'{name} joined the chat'
        self._broadcast(msg)
        thread = threading.Thread(target=self._handle, args=[name, conn])
        thread.start()

    def start(self):
        thread = threading.Thread(target=self._connect)
        thread.setDaemon(True)
        thread.start()




