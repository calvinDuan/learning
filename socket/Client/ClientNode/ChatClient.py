import socket
import threading
from Tools.Config import Standard
from Tools.Signals import Signals


class ChatClient:
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._input_name = False
        self._signals = Signals()
        self._signals.send_signal.connect(self._send)

    def _receive(self):
        while True:
            msg_len = self._client.recv(Standard.HEADER_SIZE).decode(Standard.FORMAT)
            try:
                msg_length = int(msg_len)
                msg = self._client.recv(msg_length).decode(Standard.FORMAT)
                if msg == 'Please enter your user name':
                    self._input_name = True
                self._signals.display_signal.emit(msg)
            except:
                self._client.close()
                break

    def _send(self, msg: str):
        if self._input_name:
            self._client.send(msg.encode(Standard.FORMAT))
            self._input_name = False
        else:
            buffered_msg = f'{len(msg):<{Standard.HEADER_SIZE}}' + msg
            self._client.send(buffered_msg.encode(Standard.FORMAT))

    def start(self):
        self._client.connect((Standard.HOST, Standard.PORT))
        thread = threading.Thread(target=self._receive)
        thread.setDaemon(True)
        thread.start()
