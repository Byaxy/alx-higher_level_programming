#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
 to the passed URL with the email as a parameter, and finally displays the
 body of the response.
 + The email must be sent in the variable email
 + You must use the packages requests and sys
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
