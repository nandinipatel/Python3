#Author: Nandini Patel
#Date: April 20, 2020
#Description: Learning boolean expression in Python

# day = "Friday"
# temp = 30
# raining = False

# if (day == "Saturday" and temp > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

#Let's see what evaluates to false!
#0 is false
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
