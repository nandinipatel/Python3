#Author: Nandini Patel
#Date: April 21, 2020
#Description: A challenge covering the following concepts: blocks, conditions, comparisions

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome {} to the holiday".format(name))
else:
    print("Sorry, you cannot join the holiday")