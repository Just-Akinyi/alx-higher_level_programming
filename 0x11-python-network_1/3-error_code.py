#!/usr/bin/python3
'''
takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
'''
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    myUrl = argv[1]
    req = Request(myUrl)
    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
