import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 80  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
conversation = ''
while conversation != 'exit':
    conversation = input("type smt ")
    s.sendall(bytes(conversation.encode("utf8")))
    data = s.recv(1024)
    print('Received', data.decode("utf8"))