#Author: Nandini Patel
#Date: April 18, 2020
#Description: Learning blocks and statements

#input function returns a string
name = input("Please enter your name: ")
age = (int)(input("How old are you, {0}? ".format(name))) #can typecase the input to int since age is a number

print(age)

#testing conditions with an if block
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")