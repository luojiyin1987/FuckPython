import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 3000))
sock.listen(5)
while 1:
    cli_sock, cli_addr = sock.accept()
    req = cli_sock.recv(4096)
    cli_sock.send(b'hello world')
    cli_sock.close()
