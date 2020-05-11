#Author: Nandini Patel
#Date: April 27, 2020
#Description: Python Sets

#In Python, sets are unordered, it doesn't contain duplicate; elements are immutable

#Method 1 to create a set
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

#Method 2 to create a set
#One reason to use it this way is to create an empty set
wild_animals = set(["lion", "tiger", "panther"]) #passed a list to set built in function
print(wild_animals)

for animal in wild_animals:
    print(animal)

#To add an element to sets
farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

print("=" * 40)
even = set(range(0, 42, 2))
print(even)
print(len(even))

square_tupple = {4, 6, 16}
squares = set(square_tupple)
print(squares)
print(len(squares))

print(even.union(squares)) #can do union of two sets
print(len(even.union(squares)))
 
print(even.intersection(squares)) #can find the intersecrion of two sets
print(len(even.intersection(squares)))
print("=" * 40)

#We can also subtract sets
print(sorted(even))
print(sorted(squares))

print("even minus square")
#two ways below
print(sorted(even.difference(squares)))
print(sorted(even - squares))
print("=" * 40)

print(sorted(even))
print(squares)
even.difference_update(squares) #changes made on even set
print(sorted(even))
print("=" * 40)

print("symmetric even minus squares")
print(even.symmetric_difference(squares)) #opposite of intersection; everything that is not in intersection
print("=" * 40)

#updating symetric_difference

#discard or remove can be used to delete elements from a set; only diff: remove creates an error if there is not an element to delete 
squares.discard(4)
squares.remove(16)
squares.discard(8) #no error, does nothing; 8 doesn't exist
print(squares)
#squares.remove(8) #would cause an error

#let's look at sub and super sets
if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a super of squares")

#frozensets are sets which cannot be changed; immutable
even = frozenset(range(0, 100, 2))
print(even)
#even.add(3) #would cause an error