#!/usr/bin/python3
'''
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response
'''
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    myUrl = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")

    req = Request(myUrl, data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
