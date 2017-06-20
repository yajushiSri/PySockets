#!/usr/bin/python

import socket

while 2>1:
	x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
	msg=raw_input("Enter message:")
#sendto() binds with it the address of this node. Therefore, we don't have to specify the same in order to receive a messsage.	
	x.sendto(msg,("",8888))
#recvfrom() accepts the data sent over the network.
	print x.recvfrom(100)


