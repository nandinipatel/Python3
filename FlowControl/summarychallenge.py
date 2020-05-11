#Author: Nandini Patel
#Date: April 21, 2020
#Description: Summary challenge

choice = -1

while choice != "0":
    if 1 <= choice <= 5:
        print("You have choosen option {}".format(choice))
    else:
        print("Please choose your option from the list below: ")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print("0.\tExit")
    
    choice = (int)(input())