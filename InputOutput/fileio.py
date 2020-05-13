#Author: Nandini Patel
#Date: May 4, 2020
#Description: Reading from a text file

jabber = open("original.txt", 'r') #opens a text file; 'r' stands for reading-purpose

for line in jabber:
    if "jabberwock" in line.lower(): #only checks for a specific word
        print(line, end='')

jabber.close() #closes the text file

print("-" * 40)
#using with, it will automatically close a file when it is no longer needed
with open("original.txt", 'r') as jabber: #here file is referred as jabber
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')