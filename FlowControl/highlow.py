#Author: Nandini Patel
#Date: April 22, 2020
#Description: Learning binary search

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1 #won't require more than 10 guesses
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                    "Enter h or l, or c if my guess was correct "
                    .format(guess)).casefold() #guaranteed lowercase conversion
    if high_low == "h": 
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))