# #Dictionaries
import string
x = dict()
print(x)

x['one'] = 'uno'
x['two'] = 'dos'
x['three'] = 'tres'
x['four'] = 'quatros'

print(x)
print (x['one'])

print ('uno' in list((x.values())))

# # Write a program that reads the words in words.txt and stores them as
# # keys in a dictionary. It doesn’t matter what the values are. Then you
# # can use the in operator as a fast way to check whether a string is in the
# # dictionary.

big_dict = dict()
ask = input('File name (press F) or text (press T)? ') #just putting my own spin

try:
    if ask == 'F':
        fhand = input("What is your file name? ")
        file_name = open( fhand, 'r')
    elif ask == 'T':
        file_name = input('What text are you trying to count its characters?')
    for line in file_name:
        line = line.lower()
        line = line.strip()
        line = line.split() #'uncommenting' this line will tell you about the words
        for word in line:
        # if word in big_dict: //these next four lines can be replaced with dictionary get() method
        #     big_dict[word] = big_dict[word] + 1
        # else:
        #     big_dict[word] = 1
            big_dict[word] = big_dict.get(word, 0) + 1 #Wow!
except:
    print ('Please enter T or F')
    quit()


print (big_dict)
print ('book' in big_dict)
print (big_dict.values())
print(big_dict.get('W')) 

# #prints words that appear more than once
for key in big_dict:
    if big_dict[key] > 1:
        print(key, big_dict[key])

# #sort the keys from alphabetically
list_big_dict = list(big_dict)
list_big_dict.sort()
print ('First file')
for key in list_big_dict:
    print (key, big_dict[key])

# #sort, remove punctuations in the romeo-full text, count the number of words too and display result in a dictionary file
dictionary = dict()
file_name = input('File name? ')
try:
    fhand_2 = open(file_name,'r')
    for line in fhand_2:
        line = line.strip()
        line = line.translate(line.maketrans('','',string.punctuation))
        line = line.split()
        for word in line:
            dictionary[word] = dictionary.get(word, 0) + 1
except:
    print ('Error, enter a valid file name')
    exit()


print('Second file')
list_dictionary = list(dictionary)
list_dictionary.sort()
for x in list_dictionary:
    print (x, dictionary[x])
    
    
# Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

# Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.


bigger_dict = {}
email_dict ={}
file_name3 = input('File name?')
try:
    fhand3 = open(file_name3, 'r')
    for line in fhand3:
        if line.startswith('From'):
            line = line.split()
            if len(line) > 2:
                date = line[2]
                email = line[1]
                bigger_dict[date] = bigger_dict.get(date, 0) + 1
                email_dict[email] = email_dict.get(email, 0) + 1
except:
    print('Error! Input correct file name')
    quit()

print (email_dict)

convert_list = list(bigger_dict.keys())
convert_list.sort()
for y in convert_list:
    print (y, bigger_dict[y])





