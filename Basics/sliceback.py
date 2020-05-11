#Author: Nandini Patel
#Date: April 14, 2020
#Description: Learning how to perform backwards slicing

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1] #omit the stop value to include 'a' in the string
print(backwards)

#[start:end(not including end value):slice quantity]
#[::-1] is a Python idiom for reversing a string
print(letters[-4:])
print(letters[-1:])
print(letters[:1])

#slice producing qpo
print(letters[16:13:-1])

#edcba
print(letters[4::-1])

#last 8 chars, in reverse order
print(letters[25:25-8:-1])