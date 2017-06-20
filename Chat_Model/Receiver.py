#!/usr/bin/python
#Import modules socket and os.
import socket,os
#Creates a socket, socket.AF_INET is for IPv4 and socket.SOCK_DGRAM is for UDP protocol.
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind() takes one argument only. bind() passes the address and port number of this node as its arguments.
x.bind(("",8888))
while 4>3:
	data=x.recvfrom(100)
	print data[0]
	file=open('chat_backup.txt','a+')
#This makes a file object and the filename is chat_backup.txt whose mode is set to append and write.
	file.write("Client node's message:")
	file.write(data[0])
	msg=raw_input("Enter message:")
	file.write("Server node's message:")
	file.write(msg)
	x.sendto(msg,data[1])
	file.close()
	
