#Author: Nandini Patel
#Date: April 19, 2020
#Description: Learning and/or in conditions

age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
#     print("Have a good day at work")

if 16 in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")