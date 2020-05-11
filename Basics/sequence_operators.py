#Author: Nandini Patel
#Date: April 15, 2020
#Description: Learning sequence operators in Python

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("Hello " * 5) #will print the string hello 5 times
print("Hello " * (5 + 4))

#checking for substring
#the in operator evaluates to true if the first thing exists in the second and if it doesn't, then false
today = "monday"
print("day" in today) #true
print("mon" in today) #true
print("thur" in today) #false
print("parrot" in "fjord") #false