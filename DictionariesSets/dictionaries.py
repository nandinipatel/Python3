#Author: Nandini Patel
#Date: April 23, 2020
#Description: Python Dictionaries

#Python dictionaries and set cannot be accessed using index; are unordered and accesssed by keys
#The values don't have to be the same type; we can add to a dictionary
#Two key methods: split and join

fruit = {"orange": "a sweet orange citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "apple": "round and crunchy"} #this apple value will be updated  at key 2

#To print the entire dictionary:
    # print(fruit)

#To access a particular element:
    # print(fruit["lemon"])

#To add an element to a dictionary:
    # fruit["pear"] = "an odd shaped apple"
    # print(fruit)

#When you enter the same key, it replaces the content of the old key with the new one
    # fruit["pear"] = "great with tequila"
    # print(fruit)

#To delete a key in the dictionary
    # del fruit["lemon"]
    # print(fruit)

#To delete all entries
    # fruit.clear()
    # print(fruit)

#.get() message allows us to get the value at a specific key. Returns its value if it exists or NONE

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     #prints the value(first param) if key exist otherwise it prints the second value
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)

# for snack in fruit:
#     print(fruit[snack])
# print(fruit.keys()) #returns a sorted list with all the keys

print(fruit)
print(fruit.items())