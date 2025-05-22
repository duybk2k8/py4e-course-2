# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
n = input('Enter URL: ')
x = input('Enter count: ')
y = input('Enter position: ')

for i in range(int(x)):
    url = n
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    l = list()
    for tag in tags:
        link = tag.get('href', None)
        l.append(link)
    n = l[int(y) - 1]
    print('Retrieving:',n)

    