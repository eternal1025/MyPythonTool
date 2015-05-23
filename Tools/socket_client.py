# coding:utf-8

from socket import *

HOST = 'localhost'
POST = 21322
BUFSIEZ = 1024
ADDR = (HOST, POST)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # 创建客户端套接字
tcpCliSock.connect(ADDR)					# 尝试连接服务器

while True:
 	data = raw_input('> ')
 	if not data:
 		break
 	tcpCliSock.send(data)					# 发送
 	data = tcpCliSock.recv(BUFSIEZ)			# 接受
 	if not data:
 		break

 	print '返回:', data

tcpCliSock.close()