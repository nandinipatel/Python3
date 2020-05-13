#Author: Nandini Patel
#Date: May 4, 2020
#Description: Shelve Module in Python

#data is stored in memory; similar to a dictionary
#shelves are read-write by nature
import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"

#we can access values like in dictionary in shelve files
#you cannot initialize a shelve using a literal

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    
    description = fruit.get(shelf_key)
    print(description)

fruit.close()

#to append to a shelve, you need to create another list copy the conents before, make changes, copy it back to the original