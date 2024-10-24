import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup #beautiful soup is installed, the squiggly yellow line is a warning rather than an absolute error, it means bs4 is not in my current folder
#bs4 is installed globally and accessed through my python interpreter, so no problem at all
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser') #only line worth taking a closer look at

#testing few BeautifulSoup method learnt on RealPython.com
print(soup.find_all('p'))
print(soup.get_text())

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag.get('href', None))
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)





