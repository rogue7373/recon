#!/usr/bin/python3

# import system libraries
import sys
import requests
import socket
import json

# error control
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

# URL input from user for get request and banner grabbing
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

# Print statement to display the IP address information
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n")

#ipinfo.io API call to get the location information
req_two = requests.get("https://ipinfo.io/" +gethostby_+"/json")
resp_ = json.loads(req_two.text)

# Print statement to display the location information
print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])


