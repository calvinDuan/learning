import socket

host = socket.gethostbyname(socket.gethostname())
PORT = 5050
HEADERSIZE = 10

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, PORT))
server.listen()

communication_socket, address = server.accept()
print(type(communication_socket),type(address))

while True:
    print(f'Communication with {address} has been established!')
    current_msg = ''
    full_msg = ''
    new_msg = True
    while True:
        msg = communication_socket.recv(15).decode('utf-8')
        if new_msg:
            print(f'new message length:{msg[:HEADERSIZE]}')
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
            full_msg += msg[HEADERSIZE:]
        else:
            full_msg += msg
        if len(full_msg) == msg_len:
            print(f'{full_msg}')
            print(f'Full message received!')
            current_msg = full_msg
            break
    if current_msg != 'bye':
        print(f'Please Respond: ')
        respond_msg = input()
        communication_socket.send(respond_msg.encode('utf-8'))
    else:
        communication_socket.close()
        print(f'Connection with {address} ended')
        break



