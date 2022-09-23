#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response
'''
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
