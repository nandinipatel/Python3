#Author: Nandini Patel
#Date: April 21, 2020
#Description: Learning how to use for loops

parrot = "Norwegian Blue"

#character is a user-defined variable 
#starts at the first character and runs until parrot's size
for character in parrot:
    print(character)

number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

print()

for char in number:
    if not char.isnumeric(): #check if a character is not a numeric value using isnumeric() method
        separators = separators + char #append all the non-numeric values 

#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))