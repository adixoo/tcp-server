import socket

HOST = '192.168.29.182'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # message = input("Enter a message to send: ")
    # s.sendall(message.encode())
    data = s.recv(1024)
    print('Received', repr(data))

# s.close()
