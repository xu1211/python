import socket
import sys
from socket import *
from time import ctime
'''发送tcp报文'''

def tcpSend(ip,port,en,msg):
    address = (ip, int(port))
    client = socket(AF_INET, SOCK_STREAM)#创建socket对象
    client.connect(address)#连接服务器

    #编码
    request = enCode(en,msg) #msg.encode(encoding='utf8')
    #print (request)
    client.send(request)

    data = client.recv(10240)
    #解码
    response = deCode(en,data) #data.decode(encoding='utf8')
    #print (response)

    #关闭客户端
    client.close() 
    return response

def enCode(en,msg):
    '''编码转换'''

    if en == "utf8":
        return msg.encode(encoding='utf8')
    elif en == "gbk":
        return msg.encode(encoding='gbk')
    elif en == "base64":
        return msg.encode(encoding='base64')
    else:
        return msg

def deCode(en,msg):
    '''解码转换'''

    if en == "utf8":
        return msg.decode(encoding='utf8')
    elif en == "gbk":
        return msg.decode(encoding='gbk')
    elif en == "base64":
        return msg.decode(encoding='base64')
    else:
        return msg