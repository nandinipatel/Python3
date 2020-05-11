#Author: Nandini Patel
#Date: May 11, 2020
#Description: Raw String

a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

#raw string would print the string exactly the way it is (not consider any escape characters)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslah_string = "this is a backslash \\followed by some text"
print(backslah_string)

error_string = r"this string ends with \\" #cannot end it with one backlash