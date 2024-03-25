#!/usr/bin/python3
"""
    A script that sends a request to the URL and displays the
    value of the X-Request-Id found in the response
"""

import urllib.request
import sys

def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    main()
