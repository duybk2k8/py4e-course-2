import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2215209.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
# Tìm tất cả các thẻ <count> nằm ở bất kỳ đâu trong cây XML (tree) và lưu chúng vào danh sách counts
s = 0
nums = list()
for result in counts:
    # Debug print the data :)
    nums.append(result.text)
    s = s+ int(result.text)

print('Count:', len(nums))

print('Sum:', s)
