#tuple
t = 'a','b','c','d'
print(type(t))

u = ()
print(type(u))

# For example, suppose you have a list of words and you want to sort them from
# longest to shortest:

txt = 'but soft what light in yonder window breaks'
txt = txt.split()
v = []
for word in txt:
    v.append((len(word), word))
v.sort(reverse=True)
print (v)
print (type(v))

res = []
for length, w in v:
    res.append(length)
print (res)

uname, domain = 'meleyotanoyeleke@student.lautech.edu.ng'.split('@')
print (uname, domain)

d = {'a':10, 'b':1, 'c':22}
list_of_tuples = list(d.items()) 
list_of_tuples.sort() #sorting by key
print (list_of_tuples)

large_list = []
for key, val in list_of_tuples:
    large_list.append((val, key)) #putting it in another list having values first
    large_list.sort(reverse=True) #sort by value
print (large_list)

print(d.get('a'))

for key, val in list(d.items()): #convert dictionary to list of tuples, traverse the list of tuples with two iteration variable
    print(val, key)

dictionary = {}
fhand = open('romeo.txt', 'r')
for line in fhand:
    line = line.strip()
    line = line.split()
    for word in line:
        dictionary[word] = dictionary.get(word, 0) + 1

#sort the dictionary by value

big_list = []
for key, val in list(dictionary.items()):
    big_list.append((val, key))
big_list.sort(reverse=True)

print (big_list[:5])

import re
count = 0
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line): #the wildcard is expanding to match every character before the @sign, if there are more @signs after the first, it pushes to include the characters
        count += 1
        print (line)
print(count)

t = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Return-Path: <postmaster@collab.sakaiproject.org> for <source@collab.sakaiproject.org>; Received: (from apache@localhost) Author: stephen.marquard@uct.ac.za"

another_hand = open('mbox-short.txt', 'r')
x = another_hand.read()

emails = re.findall('\S+@\S+', x) #\S means any character that is non white space
if len(emails) > 0:
    print (emails)
print (len(emails))

#some of the email addresses have weird characters starting or ending them, to remove, change regular expression
no_weird_emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', x)
print (no_weird_emails)

an_hand = open('mbox-short.txt', 'r')

#find lines that start with string X, remove the number part, 
total_z = []
total_z1 = []
total_z1_stripped = []
for one in an_hand:
    one = one.strip()
    z1= re.findall('^From .* ([0-9][0-9].* )', one)
    z = re.findall('^X\S*: ([0-9.]+)', one)#extract for the number part
    if len(z) >0: #loop through the list returned in order to change each number to float
        for each in z:
            each= float(each)
            if each > 0:#remove zeros
                total_z = total_z + [each] #append it to a list
    if len(z1) > 0:
        total_z1 = total_z1 + z1
for a in total_z1:
    a = a.strip() 
    total_z1_stripped = total_z1_stripped + [a]

print(len(total_z), total_z)
print(len(total_z1_stripped),total_z1_stripped) 

#convert list to dictionary
dict_values = {}
for one in total_z:
    dict_values[one] = dict_values.get(one, 0) + 1
print(dict_values)

# extract all of the revision numbers (the integer number at the end of these lines): 'Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772'
extract_from = 'Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772'
extracted = re.findall('^D\S.*: .*rev=([0-9]+)', extract_from)
print (extracted)




# Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

# Write a program to look for lines of the form: New Revision: 39772
regular = '^N.*: [0-9]*'

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

#!!!you have to know how it works before using comments to convert the solution below to fit exercise 1 alone

handle = open('mbox-short.txt', 'r')
# your_expression = input('Expression? ')
combined_revision = []
combined_revision_float = []
count = 0
# z = str(your_expression)
for line in handle:
    line = line.strip()
    # y = re.findall(z, line)
    u = re.findall('^N.*: ([0-9]*)', line)
    # if len(y)>0:
    #     print (line)
    #     count += 1
    if len(u) > 0:
        combined_revision = combined_revision + u

for i in combined_revision:
    i = float(i)
    combined_revision_float += [i]

total = 0
for e in combined_revision_float:
    total += e

print('This is combined revision', combined_revision)
print ('Total:',total, 'Count: ', len(combined_revision_float), 'Average: ', total/len(combined_revision_float), combined_revision_float)
# print (count)

