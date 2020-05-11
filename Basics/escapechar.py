#Author: Nandini Patel
#Date: April 12, 2020
#Description: Learning how to escape characters in Python

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)
#\n causes the string to start a new line

tabbedStr = "1\t2\t3\t5"
print(tabbedStr)
#\t causes the string to create a tab

#Let's learn the three ways to use character
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".') #used single quotes
#or we can do...
print("The pet shop owner said \"no, no, 'e's uh,...he's resting\".") #used double quotes
#or...
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting". """) #used triple quotes

anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)
#Note: backlash joins the strings that is separated by each line. Try removing the backlash and see what happens!

#Let's learn how to include backslash character in the string
print("C:\\Users\\NandiniPatel\\notes.txt") #by adding a backlash with every backlash that exists, we are telling Python that we want \
#or...
print(r"C:\Users\NandiniPatel\notes.txt") #r is a raw string which treats everything written as a string and nothing else