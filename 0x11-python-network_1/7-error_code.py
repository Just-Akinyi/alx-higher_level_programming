#!/usr/bin/python3
'''
takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
'''
from requests
from sys import argv

if __name__ == "__main__":
    myUrl = argv[1]
    req = requests.get(myUrl)
    if req.status_code > 400
        print("Error code: {}".format(err.code))
    else:    
        print(res.text)
