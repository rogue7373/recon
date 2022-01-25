#!/usr/bin/python3

# This script will attempt to crack md5 hashes. Usage is as follows: 
# python3 password_hash_cracker.py -md5 <hash> -w <wordlist>

# Imported modules
import hashlib
import argparse

# Create Parser
parser = argparse.ArgumentParser(description="MD5 Cracker")
parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)
parser.add_arguement("-w", dest="wordlist", help="wordlist", required=True)
parsed_args = parser.parse_args()

def main():
    hash_cracked = ""
    with open(parsed_args.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parsed_args.hash:
                hash_cracked = line
                print("\nMD5-hash has been cracked, the value is %s".%line)
        if hash_cracked == "":
            print("\nFailed to crack the hash, try harder.")
if __name__ == "__main__":
    main()
