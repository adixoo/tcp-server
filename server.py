import socket

HOST = '192.168.29.182'  # Standard loopback interface address (localhost)
PORT = 80        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        se = input("Enter command: ")

        # data = conn.recv(1024)
        # if not data:
        #     break
        # print(data)
        conn.sendall(se.encode('utf8'))

# conn.close()
