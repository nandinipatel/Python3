from player import Player #refer to the player class as "Player"

#don't use getters and setters in Python since no objects are hidden!
#getter: a method used to get the value of a class data attribute
#setter: a method used to set the value of a class data attribute

from enemy import Enemy, Troll, Vampyre, VampyreKing

king = VampyreKing("King")
print(king)
king.take_damage(12)
print(king)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll)) 

# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))

# brother = Troll("Urg")
# print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

# test_vamp = Vampyre("Vamp")
# print(test_vamp)
# test_vamp.take_damage(2)
# print(test_vamp)

# print('-' * 40)
# another_troll.take_damage(30)
# print(another_troll)

# # while test_vamp.alive:
# #     test_vamp.take_damage(1)

# test_vamp._lives = 0
# test_vamp._hit_points = 1
# print(test_vamp)

#===========================================
#Overloading a method: providing a method to load the values of that from its superclass
#In Python, you can't overload but you can initalise values with different number of parameters by giving a method 
#the method parameters can have default values


#Similarly, print functions can take many number of arguments

#Overriding method: change a behaviour of a sub class
#===========================================
#Polymorphism: Objects can be more than one thing at the same time (ex. a color is a color but there also can be a red color or a blue color)