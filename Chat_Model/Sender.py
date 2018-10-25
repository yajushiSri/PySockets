#!/usr/bin/python

import socket

while True:
	soc_var = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	
	msg = input("Enter message:")
#sendto() binds with it the address of this node. Therefore, we don't have to specify the same in order to receive a messsage.
#Replace "Receiver_IP" with the receiver's IP address. Here, "8888" is the specified port number of receiver node.
	soc_var.sendto(msg,("Receiver_IP",8888))
#recvfrom() accepts the data sent over the network.
	print( soc_var.recvfrom(100))


