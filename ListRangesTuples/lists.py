#Author: Nandini Patel
#Date: April 22, 2020
#Description: Learning lists

# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count(".")) #count() allows us to count what's inside ("")
# print()

# parrot_list = ["non pinin", "no more", "a stiff", "berefit of live"]
# parrot_list.append("A Norwegian Blue")

# for state in parrot_list:
#     print("This parrot is " + state)
# print()

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = even + odd #appending two lists
# numbers.sort() #sorts method works(sorts) on the existing method and does not return anything

# print(sorted(numbers)) #sort is a function that returns a new list of sorted numbers

list_1 = []
list_2 = list() #creating a list using the list constructor

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

print(list("The lists are equal")) #creating a list with each character stored according to the string
print() 

even = [2, 4, 6, 8]
another_even = sorted(even, reverse = True)
print(even)

#is refers to the location in memory when comparing when == refers to the content