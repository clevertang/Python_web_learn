# -*- coding: utf-8 -*-
__author__ = "clevertang"
import socket
# 常量大写
HOST = "localhost"
PORT = 3434
# AF_INET说明使用IPV4地址,SOCKET_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("sb".encode())
print("连接成功:{}:{}".format(HOST,PORT))
data=s.recv(1024)#制定接收数据的最大长度
print("收到消息{}".format(data))
s.close()