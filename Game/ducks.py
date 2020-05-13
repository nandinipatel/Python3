#Author: Nandini Patel
#Date: May 12, 2020
#Description: Polymorphism in Python

#Python focus more on how objects behave rather than how its written
#Inheritance: is-a relationship 
#Composition: has-a relationship

class Wing(object):
    #default constructor
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard word, but I'm flying")
        else:
            print("I think I'll just walk")

class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)  #created a new attribute (composition)

    def walk(self):
        print("Waddle, waddle, waddle")
    
    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):
    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

if __name__ == "__main__":
    #calls the default constructor if there is one
    donald = Duck()
    donald.fly()