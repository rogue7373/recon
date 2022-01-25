#!/usr/bin/python3

# Import modules
import socket

# create host listener and defined port. Port can be changed to preferred port number
host = socket.gethostname()
port = 6969

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_.bind((host,port))
sock_.listen(1)

print("\nServer started...\n")

conn,addr = sock_.accept()

print("Connection established with: ", str(addr))

message = "\nI'm in, connected to " + str(addr)
conn.send(message.encode("ascii"))
conn.close()

