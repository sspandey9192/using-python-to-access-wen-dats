import urllib.request, urllib.parse, urllib.error
import json
import ssl

url=input('enter url--    ')

print('Retrieving', url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#print(data)
js=json.loads(data)
count=0
p=len(js['comments'])
print('Count : ',p)
for i in range(p):
    count+=js['comments'][i]['count']
print('sum : ',count)
#lat = js['comments'][i]['geometry']['location']['lat']
