#Author: Nandini Patel
#Date: April 13, 2020
#Description: Learning how to string in depth 

parrot = "Norwegian Blue"

print(parrot)
print(parrot[3]) #accessing index of a string
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

#to get negative index of a value, simple do the current value - size
print(parrot[-11]) #using negative indexing to print the same statement
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

#Let's learn slicing
print(parrot[0:6]) #Start at position 0 and upto position 6(not including 6)
print(parrot[3:5]) #we
print(parrot[:9]) #start value is understood to be at the start of the sequence
print(parrot[10:]) #similarly, if the end value is not writtenm it is understood to be at the end of the sequence

#negative slicing:
print()
print(parrot[-14: -8]) 
print(parrot[-11: -9])
print(parrot[:-5])
print(parrot[-4:]) 

print()
print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw