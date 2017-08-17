#  -*- coding: utf-8 -*-  
__author__ = 'clevertang'
#学习如何控制台调用程序，以及增加参数
import sys

# params = None
# if len(sys.argv) ==3:
#     params = int(sys.argv[1])
# if params is None:
#     print("alert")
#     print("the param is not set")
#
# elif params <-10:
#     print("the param is small")
#
# elif params>10:
#     print("the param is big")
# else:
#     print("the param is middle")
import sys
print ("脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):
    print ("参数", i, sys.argv[i])