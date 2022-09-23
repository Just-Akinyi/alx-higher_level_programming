#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response
'''
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    myUrl = argv[1]

    r = Request(myUrl)
    with urlopen(r) as response:
        print(response.headers.get("X-Request-Id"))
