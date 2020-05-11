#Author: Nandini Patel
#Date: April 17, 2020
#Description: Learning string formatting in Python

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
    #{0:#} number separated by the colon represents the width for formatting

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))
    #< makes the formatting left-align, > would be right-align, ^ center within the field

print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))