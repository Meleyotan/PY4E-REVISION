#write into a new file
file_name = input('Enter the file name: ')
line1= 'My name is Meleyotan'
line2= 'My name is also Daniel'
fhand = open(file_name, 'w')
fhand.write(line1)
fhand.write(line2)

#continuosly write into a file, challenge: the newline character is not evaluating when I put it in a string response to input

try:
    line = " "
    while True:
        x = input("What do you like to write?")
        x = str(x)
        print(type (x))
        fhand = open(file_name, 'w')
        if x == 'done': break
        line = line + x
        fhand.write(line)
    fhand.close()
except:
    print ('File cannot be opened')
    exit()

#reading a file into a single variable

inp = fhand.read()
print (len(inp))
print (inp[:20])

#count the number of lines that starts with "From"

count = 0
for line in fhand:
    if line.startswith("From"):
        line = line.strip()
        print (line)
        count = count + 1
print ('The total of lines that starts with \'From\':', count)

#find the lines with the '@uct.ac.za'
for line in fhand:
    line = line.strip()
    if line.find('@uct.ac.za') == -1:
        continue
    print (line)

# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

file_name2 = input("What is the file name for this exercise? ")
fhand2 = open(file_name2, 'r')
for f in fhand2:
    f = f.strip()
    print (f.upper())

# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475

file_name3 = input("What is the name of the file for this exercise? ")
try:
    fhand3 = open(file_name3, 'r')
    count = 0
    total = 0
    for f in fhand3:
        f = f.strip()
        if f.find('X-DSPAM-Confidence:') == -1: continue
        position = f.find(' ')
        z = float(f[position:])
        count = count +1
        total = total + z 
        print('Count: %g, Total: %g, Average: %g' % (count, total, (total/count)))
except:
    print ("Error, please input a valid file name")

file_name4 = input("What is the name of your file? ")
if file_name4 == "na na boo boo":
    print ("you have been punk'd")
    exit()
try:
    fhand4 = open(file_name4, 'r')
    print(fhand4)
except:
    print("Error, please enter a correct file type")
    exit()


    