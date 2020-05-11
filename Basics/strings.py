#Author: Nandini Patel
#Date: April 11, 2020
#Description: Learning how to use string in Python

print("Today is an amazing day to learn Python")
print('Python is fun')
print("Python's string are easy to use") #double quote
#There is no difference between single or double quote string in Python; simply match the start and end string

print('We can even include "quotes" in strings')
print("hello" + " world") #string concatenation 

#We can store string in variables. Let's see how:
greeting = "Hello"
name = "Bruce"
print(greeting + ' ' + name)

#Let's use the input function to read string from the user
name1 = input("Please enter your name: ")
print("Hello " + name1)

#Note: input is a function that allows us to get user input and the return value would be stored in a variable
#In the case above, the return value would be a string, assigned to name1

print(type(greeting)) #to find out what data type a variable Python think it is
age_in_words = "2 years" #binding data types
print(type(age_in_words))

age = 24
print()
print(name + f" is {age} years old")
print(f"Pi is approximately {22/ 7:12.50f}")