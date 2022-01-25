# recon
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