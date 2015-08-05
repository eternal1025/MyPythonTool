# coding:utf-8

#-----------------------
# TCP时间戳服务器
#-----------------------

from socket import *
from time import ctime

HOST = ''
POST = 21322
BUFSIEZ = 1024
ADDR = (HOST, POST)

tcpSerSock = socket(AF_INET, SOCK_STREAM)      # 创建服务器套接字
tcpSerSock.bind(ADDR)						   # 把地址绑定在套接字上
tcpSerSock.listen(5)						   # 监听连接

while True:
	print '等待连接...'						   # 服务器无限循环
	tcpCliSock, addr = tcpSerSock.accept()	   # 接受客户端连接
	print '连接来自:', addr 					   

	while True:								   # 通讯循环
		data = tcpCliSock.recv(BUFSIEZ)        # 接收
		if not data:
			break

		print '接受到:', data
		tcpCliSock.send('[%s] %s' % (ctime(), data)) # 发送
		# tcpCliSock.close()   # 关闭客户端套接字

tcpSerSock.close()   #关闭服务器套接字