#!/usr/bin/python3
# Mac address spoofing for linux machines

# Import modules
import random
import os 
import subprocess

# Define def for random generation of mac address

def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    new_ = ""
    for i in range(0,5):
        new_ += get_rand()+get_rand()+":"

    new_+=get_rand()+get_rand()
    return new_

# Grep for current Mac Address 
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

# Take down the current eth0 
subprocess.call(["sudo", "ifconfig", "eth0", "down"])


# Assign new mac address 
new_m = new_mac()
subprocess.call(["sudo","ifconfig", "eth0", "hw", "ether", "%s"%new_m])

# Bring up the new eth0
subprocess.call(["sudo", "ifconfig", "eth0", "up"])

# Print newly assigned Mac Address
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

