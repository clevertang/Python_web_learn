#  -*- coding: utf-8 -*-  
__author__ = 'clevertang'
#学习如何控制台调用程序，以及增加参数
import sys

params = None
if len(sys.argv) > 1:
    params = int(sys.argv[1])
if params is None:
    print("alert")
    print("the param is not set")

elif params <-10:
    print("the param is small")

elif params>10:
    print("the param is big")
else:
    print("the param is middle")
