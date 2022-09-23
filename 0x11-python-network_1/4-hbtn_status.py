#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == "__main__":
    myUrl = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(myUrl) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))