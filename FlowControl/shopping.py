#Author: Nandini Patel
#Date: April 21, 2020
#Description: Learning continue and break

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item == "spam":
#         continue #will continue with other items in the iteration whenever the condition is true
#     print("Buy " + item)

# print()
# for item in shopping_list:
#     if item == "spam":
#         break #stops the iteration whenver the condition is true
#     print("Buy " + item)

item_to_find = "spam"
found_at = None #a constant used to show something doesn't have a value (or null)

#for index in range(6)
# for index in range(len(shopping_list)): #len returns how many items are in the list (0-5)
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

#But...there is an easier way to do it!

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} is not found".format(item_to_find))