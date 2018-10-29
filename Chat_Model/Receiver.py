#!/usr/bin/python
#Import modules socket and os.
import socket
import os
#Creates a socket, socket.AF_INET is for IPv4 and socket.SOCK_DGRAM is for UDP protocol.
soc_var = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind() takes one argument only, a tuple in this case. bind() passes the address and port number of this node as its arguments.
soc_var.bind( ("",8888) )
while True:
	data = soc_var.recvfrom(100)
	print data[0]
	with open('chat_backup.txt','a') as file_handle:
	#This makes a file object and the filename is chat_backup.txt whose mode is set to append and write.
		file_handle.write("Client node's message:")
		file_handle.write(data[0])
		msg = input("Enter message:")
		file_handle.write("Server node's message:")
		file_handle.write(msg)
		soc_var.sendto(msg,data[1])
