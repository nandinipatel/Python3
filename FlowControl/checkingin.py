#Author: Nandini Patel
#Date: April 21, 2020
#Description: Learning in 

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")