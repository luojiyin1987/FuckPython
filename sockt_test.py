import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 3000))
sock.send(b'GET /HTTP/1.1\r\nHost:127.0.0.1:3000\r\n\r\n')
data = sock.recv(4096)
print(data)
sock.close()
