import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url= 'http://py4e-data.dr-chuck.net/comments_1273325.xml'
uh=urllib.request.urlopen(url)
data=uh.read()
tree=ET.fromstring(data)
counts=tree.findall('comments/comment')
ist=list()
for item in counts:
    nums=item.find('count').text
    num=int(nums)
    ist.append(num)
print(sum(ist))
