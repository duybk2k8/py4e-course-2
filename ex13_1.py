import json
import urllib.request
import xml.etree.ElementTree as ET
count = 0
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2215210.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode() 
info = json.loads(data)
for x in range(len(info['comments'])):
    count += int(info['comments'][x]['count'])
print('Retrieved',len(data))
print('Count:', len(info['comments']))
print('Sum:', count)
#info có dạng dictionary
#data có dạng data
