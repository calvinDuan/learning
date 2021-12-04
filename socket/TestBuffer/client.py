import socket

HOST = '192.168.50.202'
PORT = 5050
HEADERSIZE = 10

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

is_ended = False

while not is_ended:
    msg = input()
    buffered_msg = f'{len(msg):<{HEADERSIZE}}' + msg
    client.send(buffered_msg.encode('utf-8'))
    if msg != 'bye':
        print(client.recv(1024).decode('utf-8'))
    else:
        is_ended = True