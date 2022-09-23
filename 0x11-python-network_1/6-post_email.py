#!/usr/bin/python3
'''
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response
'''
import requests
from sys import argv

if __name__ == "__main__":
    myUrl = argv[1]
    value = {"email": argv[2]}
    res = requests.post(myUrl, data=value)
    print(res.text)
