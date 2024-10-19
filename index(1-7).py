
import math
import random

# prompt to compute pay
hour = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    hour = float(hour)
    rate = float(rate)
    if hour > 40:
        pay = ((rate * 1.5) * (hour -40)) + (rate * 40)
    else:
        pay = hour * rate
    print ('Pay:', pay)
except:
    print ('Error, please enter numeric input')

# prompt to compute score
score = input ('Enter score: ')
try:
    if float(score) >= 0.0 and float(score) <= 1.0:
        if float(score) >= 0.9:
            print ('A')
        elif float(score) >= 0.8:
            print ('B')
        elif float(score) >= 0.7:
            print ('C')
        elif float(score) >= 0.6:
            print ('D')
        elif float(score) < 0.6:
            print ('F')
    else:
        print ('Bad score')
except:
    print ('Please enter a number between 0.0 and 1.0')

# testing math module
print (10 * math.log10(1000))
print (10/math.sqrt(10))

#testing random module -1
for i in range (10):
    x = random.random()
    print (x)

#testing random module -2
print(random.randint(5,7))
x = [12, 23, 34, 45, 56, 67, 78, 89, 90]
print(random.choice(x))

# function definition and calling
def print_lyric():
    x = ("I am a lumberjack and I am okay\nI sleep all night and I work all day")
    print(x)

def repeat_lyric():
    print_lyric()
    print_lyric()

# calling function
repeat_lyric()

def addtwo(x, y):
    added = x + y
    return added

# calling function
print (addtwo(3,5))
function_result = addtwo(3,5)
print (function_result)

#function to compute pay
def computepay(hours, rate):
    try: 
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            pay = ((rate * 1.5) * (hours -40)) + (rate * 40)
        else:
            pay = hours * rate
        return pay
    except:
        return ('Error, please enter numeric input')
    
c = computepay(45, 6)
print (c)

#function to compute score
def computescore(score):
    try:
        score = float(score)
        if float(score) >= 0.0 and float(score) <= 1.0:
            if float(score) >= 0.9:
                print ('A')
            elif float(score) >= 0.8:
                print ('B')
            elif float(score) >= 0.7:
                print ('C')
            elif float(score) >= 0.6:
                print ('D')
            elif float(score) < 0.6:
                print ('F')
        else:
            print ('Bad score')
    except:
        print ('Please enter a number between 0.0 and 1.0')

computescore(0.77)

# loop with iteration variable
n = 5
while n > 0:
    print ("Blastoff!")
    n = n-1
print ("Done")

# loop with break statement
while True:
    line = input ('loop with break statement>')
    if line == 'done':
        break
    print (line)

#whenever # begins statement, don't print - a code for making sure comment statements doesn't print
while True:
    line = input("> ")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print (line)
print ('Done')

friends = ['Meleyotan', 'Daniel', 'Oyeleke']
for friend in friends:
    print ("Merry Christmas, " + friend)
print ('Done')
    
sets = [6,73,23,534,23,63,12,778,344]
total = 0
for itevar in sets:
    total = total + itevar
print (total)

file_input = input("Enter file name: ")
handle = open(file_input, 'r')

for line in handle:
    words = line.split()
print (len(words))

#print the largest number in this set [1,24,5,6,77,343,3,232,3,23,1,3,43,1,3]

largest = None
numbers = [1,24,5,6,77,343,3,232,3,23,1,3,43,1,3]
for number in numbers:
    if largest is None or number > largest:
        largest = number
    print ("In this loop:", largest, "is greater than ", number)
print (largest, "is the largest")

print (max(numbers))
print (min(numbers))

smallest = None
numbers = [1,24,5,6,77,343,3,232,3,23,1,3,43,1,3]
for number in numbers:
    if smallest is None or number < smallest:
        smallest = number
    print ("In this loop:", smallest, "is lesser than ", number)
print (smallest, "is the smallest")

# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number. ***

# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

total = 0
count = 0
largest = None
smallest = None
while True:
    x = input ("What number? ")
    if x == "done":
        break
    try:
        x = float(x)
        count = count + 1
        total = total + x
        if largest is None or x > largest:
            largest = x
        if smallest is None or x < smallest:
            smallest = x 
        print ("Count:", count, "Total: ", total, "Average: ", total/count, "Max: ", largest, "Min: ", smallest)
    except:
        print ("Error, please enter a number")

#reverse a string
test = "Meleyotan Oyeleke"
n=1
count = len(test)
while n-1 < count:
    print (test[count- (count+n)])
    n = n + 1

#split a string
print (test[2:10])
print (test[:])

# count the number of "es" in a text
count = 0
for t in test:
    if t == "e":
        count = count + 1
print ("Number of Es", count)

#encapsulate the above block of code in a function
def count_letter(text, letter):
    count = 0
    for t in text:
        if t == letter:
            count = count + 1
    return "Number of As", count

print(count_letter("the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car", "a"))

#using the count method of string type
print ("Melekyotafoaefw2wu2222222222wwwwwwwwwwwww23w3eeeeeeeeeeeeeeeeeeeeeeeeeeawe".count("w"))

#format operator %d means integer, %g -float, %s-string
camel = 42
print ('I spotted %d camel' % camel)
print ('I have % d camel and %g can score' % (camel, 0.34))
print ('I have %d, %d, %d, shoes' %(14,15,19))

#to parse string
str = 'X-DSPAM-Confidence:0.8475'
first_position = str.find(':')
strs = str[first_position + 1:]
print (float(strs))
print (str)

# the str was not actually replaced, it was initiated in a new variable and allowed to modify based on what was in str
z = str.replace('X', 'Y')
print (str)
print (z)


