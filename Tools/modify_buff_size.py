#coding:utf-8
import socket

SEND_DUF_SIZE = 4096
RECV_DUF_SIZE = 4096

def modify_buff_size():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#获取套接字发送和接收缓冲区大小
	bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Buffer size [设置前]: %d" %bufsize

	sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 1)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_DUF_SIZE)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_DUF_SIZE)

	bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Buffer size [设置后]: %d" %bufsize

if __name__ == '__main__':
	modify_buff_size()
