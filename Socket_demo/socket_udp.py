# -*- coding: utf-8 -*-
__author__ = "clevertang"
#TCP的服务器端


import socket
import datetime

# 常量大写
HOST = "localhost"
PORT = 3434

# AF_INET说明使用IPV4地址,SOCKET_STREAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)  # 接收TCP连接,并返回新扽socketd对象
    print("Clinet%s连接了,%s"% (str(addr),str(data)))


s.close()
