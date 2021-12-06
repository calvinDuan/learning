from Server.MyServer import ChatServer
import time

def start():
    server = ChatServer()
    server.start()
    cmd = input()
    while True:
        if cmd == 'quit':
            break
        else:
            cmd = input()


if __name__ == '__main__':
    start()