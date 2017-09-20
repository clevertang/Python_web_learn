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

data="hello udp"
s.sendto(data.encode(),(HOST,PORT))
print("send :%s to %s:%d"%(data,HOST,PORT))
s.close()
