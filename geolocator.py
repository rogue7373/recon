#!/usr/bin/python3

import sys
import requests
import socket

if len(sys.argv) > 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://"sys.argv[1])
print("\n" +str(req.headers))

gethostby = socket.gethostbyaddr(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is " + gethostby + "\n")

#ipinfo.io API call 
ipinfo = requests.get("https://ipinfo.io/" + sys.argv[1] + "/json")
