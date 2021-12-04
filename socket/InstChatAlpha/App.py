from Server.Server import ChatServer


def start_server():
    server = ChatServer()
    server.server_start()


if __name__ == '__main__':
    start_server()