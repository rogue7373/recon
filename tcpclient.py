#!/usr/bin/python3

# Import modules
import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to server
sock_.connect((socket.gethostname(),6969))
msg = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))

