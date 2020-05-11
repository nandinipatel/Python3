#Author: Nandini Patel
#Date: April 22, 2020
#Description: Else in a loop

numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        print("the numbers are unacceptable")
        break
else: #executes if the loop terminates normally
    print("All those numbers are fine")