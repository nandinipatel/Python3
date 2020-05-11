#Author: Nandini Patel
#Date: April 21, 2020
#Description: Learning while loop

# i = 0
# while i < 10:
#     print("i is not {}".format(i))
#     i += 1

available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("aren't you glad you got out of there")

