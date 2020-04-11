import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
url=input('enter url-- ')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data=urllib.request.urlopen(url, context=ctx).read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
s=0
for i in results:
    s=s+int(i.find('count').text)
print(s)
