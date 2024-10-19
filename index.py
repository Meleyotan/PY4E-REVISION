
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
    line = input ('>')
    if line == 'done':
        break
    print (line)
