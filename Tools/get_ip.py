# coding: utf-8

"""
	获取IP地址
"""

import socket   #for sockets
import sys  #for exit

host = 'www.oschina.net'
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
