# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.
import socket
import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

HOST = input('HOST SERVER?')
PORT = 80

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))
    mysock.send(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')
    count = 0
    while True:
        data = mysock.recv(3000)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()
    for line in data:
        print (repr(line))
except:
    print ('Error, please enter proper URL')


# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire docu-
# ment and count the total number of characters and display the count
# of the number of characters at the end of the document.

mysock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock1.connect((HOST, PORT))
cmd = 'GET http://data.pr4e.org/mbox.txt HTTP/1.0\r\n\r\n'.encode()
mysock1.send(cmd)

character_length = 0
total_count = 0

while True:
    data = mysock1.recv(3000)
    if len(data) < 1:
        break
    data = data.decode()
    for character in data:
        character_length += 1
        if character_length > 3000:
            break
 
    total_count = total_count + len(data)

print('%d total characters received, %d characters printed' %(total_count, character_length))



# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

character_length1 = 0
total_count1 = 0
handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
while True:
    info = handle.read(10)
    if len(info) < 1:
        break
    total_count1 += len(info)
    for character in info:
        character_length1 += 1
        if character_length1 >=70:
            break
    mysock1.close()   
print('%d total characters received, %d characters printed' %(total_count1, character_length1))


# Exercise 4: Change the urllinks.py program to extract and count para-
# graph (p) tags from the retrieved HTML document and display the
# count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several
# small web pages as well as some larger web pages.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
# Retrieve all of the p tags and count with beautiful soup and regular expression

#if beautiful soup is used

soup = BeautifulSoup(html, 'html.parser')
count = 0
tags = soup('p')
for tag in tags:
    count += 1
    print (tag)
print (count)

# if regular expression is going to be used use 
dic ={}
count_reg = 0
links = re.findall(b'<p.*?>.*?</p>', html)
for link in links:
    print (link.decode())
    count_reg += 1
    dic[link] = dic.get(link,0) + 1
print(dic)
print (count_reg)



#stripped all spaces in https://docs.python.org and wrote into a new file

# new_test = open('new_test.txt', 'w')
# file_handle = open('test.txt', 'r')
# for line in file_handle:
#     line = line.strip()
#     print(line)
#     new_test.write(line)


    
# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.