import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
    msg=input("client>")
    s.send(msg.encode())
    print("server>",s.recv(1024).decode())