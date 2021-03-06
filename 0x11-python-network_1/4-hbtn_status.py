#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status using the packages
requests
"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
