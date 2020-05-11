#Author: Nandini Patel
#Date: May 11, 2020
#Description: OOP in Python

 # + and __add__ calls the same method in builtins.py

#Everything in Python are objects
#When a function is part of a class, its a method. Otherwise, its a function

class Kettle(object):
    #a class attribute 
    power_source = "electricity"

    #self is a reference to the instance of a class
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
    Class: template for creating objects
    Object: an instance of a class
    Instantiate: process of creating an instance of a class
    Method: a function defined in a class
    Attribute: a variable bound to an instance of a class
"""

print(hamilton.on) #print before value
hamilton.switch_on()
print(hamilton.on) #print after value

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power) #can create attributes which are not defined in methods of a class like this!
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

#all three ^ have instances of power sources

print("Switch to atomic power")
Kettle.power_source = "atomic"
print("Switch to gas power")
Kettle.power_source = "gas"
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)