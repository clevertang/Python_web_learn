# -*- coding: utf-8 -*-
"""
@author: clevertang
@license: Apache Licence 
@contact: 961577196@qq.com

@software: PyCharm Community Edition
@file: wsgi_server.py
@time: 2017/9/28 22:09
"""
# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from webapp import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8090, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()