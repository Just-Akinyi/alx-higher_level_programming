#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status
'''
import requests

if __name__ == "__main__":
    myUrl = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(myUrl)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
