#!/usr/bin/env python

import string
import requests
import json
import argparse

from pygments import highlight, lexers, formatters

__author__ = "@r3dbU7z"
__copyright__ = "Copyright 2021, @r3dbU7z "
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License."
__version__ = "0.0.1"

parser = argparse.ArgumentParser(description='Requesting IP address data from Shodan database - internetdb.shodan.io')
parser.add_argument('-a', '--addr', dest='ip_addr', help='IP address (required)', type=str, metavar="IP_ADDR", required=True) 

args = parser.parse_args()
ip_addr = args.ip_addr

internetdb_url = "https://internetdb.shodan.io/"

request_str  = '{0}{1}'.format(internetdb_url, ip_addr)
#request_str = internetdb_url + ip_addr

print("\n" + "Request: " + internetdb_url + ip_addr +"\n")

host = requests.get(request_str).json()

#print(json.dumps(host, indent=4, sort_keys=True))
formatted_json = json.dumps(host, indent=4, sort_keys=True)

#https://stackoverflow.com/questions/25638905/coloring-json-output-in-python
colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalTrueColorFormatter())
print(colorful_json)