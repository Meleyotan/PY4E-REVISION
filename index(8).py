numbers = [1,2,3,4,5,6,7,[8,7]]
for i in range(len(numbers)):
    numbers[i]= numbers[i] * 2
print (numbers)

numbers.pop(2)
print(numbers)

del numbers[1:3]
print(numbers)

#computed the average of a list of numbers entered by the user using a list.
bank = []
while True:
    number = input('Que? ')
    if number == 'done': break
    try:
        number = float(number)
        bank.append(number)
    except:
        print ("Error, please enter a number")
if len(bank) > 0:
    print('Count: %g, Total: %g, Average: % g' % (len(bank), sum(bank), sum(bank)/len(bank)))

s = 'spam-spam-spam, sapma, adfiaohfao,f fa'
x= list(s)
print (s)
print(x)
print(s.split())

#using the join() string method join takes iterable arguments
to_join = ['a','b','c','d','e','f','g']
delimeter = ' '
y = delimeter.join(to_join) #take note of this use
print (y)

# print the days of the week from "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
list_senders = []
file_name = input('entrez le nom du fichier: ')
fhand = open(file_name, 'r')
for iterey in fhand:
    iterey = iterey.strip()
    if iterey.startswith('From'):
        iterey = iterey.split()
        if len(iterey) < 3: continue
        print(iterey[2])
        list_senders.append(iterey[1])
print(list_senders)
print(len(list_senders))

#Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(ls):
    ls.pop(0)
    ls.pop(-1)
    return ls
    
ls = [1,23,4,5,6]

print(chop(ls))

ls1 = [1,2,3,4,5,6]

def middle(ls):
    return ls[1:-1]


print(middle(ls1)) 
print(middle(sorted(ls1)))

#shakespeare

# Exercise 4: Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you
# determine that? How would you produce the list of all the words that
# Shakespeare used? Would you download all his work, read it and track
# all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted
# in alphabetical order, that are stored in a file romeo.txt containing a
# subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

big_list = []
new_list = []
file_name1 = input("File name? ")
fhand2 = open(file_name1, 'r')
for line in fhand2:
    line = line.strip()
    line = line.split()
    for l in line:
        big_list.append(l)
for x in range(len(big_list)):
    if big_list[x] in new_list: continue
    new_list.append(big_list[x])
print(sorted(new_list))
print(len(sorted(new_list)))

# Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

maximum = None
minimum = None
list_of = []
    
while True:
        number_que = input("Number? ")
        if number_que == 'done': break
        try:
            number_que = float(number_que)
            list_of.append(number_que)
            if maximum is None or number_que > maximum:
                maximum = number_que
            if minimum == None or number_que < minimum:
                minimum = number_que
        except:
            print('Error, please enter a number')
print('Max: %g, Min: %g' % (maximum, minimum))

