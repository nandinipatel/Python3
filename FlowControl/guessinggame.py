#Author: Nandini Patel
#Date: April 18, 2020
#Description: Learning blocks and statements

import random #importing random function

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 #0 is to quit

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   #must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    elif guess == answer:
        print("Well done you guessed it")
    else:
        if guess < answer:
            print("Please guess higher")
        else:   #must be greater than answer
            print("Please guess lower")