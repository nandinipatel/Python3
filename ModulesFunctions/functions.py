#Author: Nandini Patel
#Date: May 08, 2020
#Description: Learning Functions in Python

#functions are created with def name parameters
def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width-len(text)) // 2
    print(" " * left_margin, text)

#*args refers to multiple arguments passed
def centre_text(*args, sep=' '):
    text = " "
    for arg in args:
        text += str(arg) + sep
    left_margin = (80-len(text)) // 2
    return " " * left_margin, text

print(centre_text("first", "second", 3, 4, "spam", sep=":"))
print("=" + str(12*3))
print(sorted(["b", "d", "c", "a"]))