# GeoLocation Recon
Python Scripts for OSINT
This python script will provide insight into IP address related to hostnames, provide geo location information. 

Example usage -- python3 geolocator.py "rt.com" 

Example output:

    {'Server': 'nginx', 'Date': 'Tue, 25 Jan 2022 01:37:52 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'x-4fna': '3brfna', 'Cache-Control': 'no-cache,no-store,max-age=0', 'X-4vcta': 'H5204N', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload, max-age=31536000; includeSubDomains; preload', 'Content-Encoding': 'gzip'}

The IP address of rt.com is: 207.244.80.179

Location: 38.8951,-77.0364
Region: Washington, D.C.
City: Washington
Country: US

*********************************************************

# Port Scanner with NMAP

Example usage -- python3 portscanner_nmap.py <IPADDRESS>

Example output -- 

Scanning 127.0.0.1 for ports 21,22,80,139,443,8080...

Port 21  is  closed
Port 22  is  open
Port 80  is  closed
Port 139  is  closed
Port 443  is  closed
Port 8080  is  closed

Host 127.0.0.1  is  up

*********************************************************

# Screen Grabber with WX Python that uploads to remote FTP /tmp folder 

Please change the following within the script to point to the FTP Server:

FTP SERVER ADDRESS
USERNAME
PASSWORD

You can also change the file destination by changing the:
sess_.storbinary 

Script will grab the active screen and upload it to a remote FTP session. Once the screenshot has been taken, exfilled to FTP the script will then close the file and the FTP session. 

*********************************************************

# Network socket TCP Server / TCP Client 

tcpserver script, creates a TCP Server listening on a specified port. 

tcpclient script, will provide a basic TCP connection back to the server. 

*********************************************************
# Network Floodz with Scapy

Script Name: networkfloodz.py 

** Warning ** 
This tool should be used to generate traffic only and not for malicious purposes.

modules: Scapy installed with pip install scapy.

User input for choice of Source, Target. 

by changing range(100,150) to an increased number will generate more packets. 

Example: range(100, 20000000) will send a large number of packets. 

*********************************************************

# Word Press Brute Force

** WARNING ** This is a tool for testing ** Not intended for malicious use **

Word press admin brute force tool. 

This has not been tested, however, this was designed after a working script. 

Update password_dictionary.txt to a wordlist of your choice. 

For testing outside of Local Host (127.0.0.1) please update any local host name or IP addressing to match the target host and IP addressing. 

*********************************************************

# Sub-Domain Recon

This script will crawl subdomains for a provided domain. 

Allows for custom sub-domain list to be provided within the script, saved in the same directory as the script. 

This could be modified to pull a sub-domain list from an API or outside source. 

*********************************************************

# Python Password/Hash cracker

Script to crack hashes created in python