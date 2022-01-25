#!/usr/bin/python3

# Sub domain enumeration tool

# Imported modules
import requests
import sys

# List of subdomains in a txt file. Update the file name subdomains-1000.txt to the file name of your choice. This file should be in the same directory as this script.

sub_list = open("subdomains-1000.txt").read() 
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://(sub).{sys.argv[1]}" 

    try:
        requests.get(url_to_check)
    except requests.ConnectionError:
        pass
    else:
        print("Valid Domain: ",url_to_check)
