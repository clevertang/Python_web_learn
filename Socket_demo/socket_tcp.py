# -*- coding: utf-8 -*-
__author__ = "clevertang"
#TCP的服务器端


import socket
import datetime

# 常量大写
HOST = "localhost"
PORT = 3434

# AF_INET说明使用IPV4地址,SOCKET_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()  # 接收TCP连接,并返回新扽socketd对象
    print("Clinet%s连接了"% str(addr))
    dt = datetime.datetime.now()
    print(dt)
    print(type(dt))
    message = "Current time is{}".format(str(dt))
    conn.send(message.encode())
    print("send: " + message)
    if "s".encode() in conn.recv(1024):
        print("你才是sb")
    conn.close()
