#!/usr/bin/env python
#coding=utf-8

import socket
import re

HOST = ''
PORT = 8000

index_content ='''
HTTP/1.x 200 ok
Content-Type: text/html
'''

file = with open('reg.html')
reg_content +=file.read()

file = with open('T-mac.jpg')
pic_content='''
HTTP/1.x 200 ok
Content-Type: image/jpg

'''
pic_content += file.read()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(100)

while True:
    conn, addr = sock.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    print 'Connect'

)

