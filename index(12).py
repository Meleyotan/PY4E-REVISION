import socket
import time
import urllib.request,urllib.parse,urllib.error
import re
import ssl

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'data.pr4e.org'
PORT = 80
mysock.connect((HOST,PORT))
cmd = b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'
mysock.send(cmd)
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
fhand = open('stuff.jpg', 'wb')
fhand.write(picture)
fhand.close()

#better style of retrieving data from the web
dictionary = {}
fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in fhand:
    line = line.decode().strip()
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
print (dictionary)

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand2 = open('image.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand2.write(info)
print(size, 'characters copied')
fhand2.close()

# fhand3 = urllib.request.urlopen('https://html.com/#The_HTMLcom_Blog') #Error 403 Forbidden
# for line in fhand3:
#     line = line.decode().strip()
#     print (line)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="http[s]?://.*?"', html)#what is this program doing? It will retrieve all the links on this html page
for link in links:
    print(link.decode())

