#Author: Nandini Patel
#Date: May 10, 2020
#Description: Learning importing techniques

#we can reused other functions using libraries
import blackjack
# print(__name__)
# blackjack.play()

# when there is _places in front of a method, it is implied that its protected tho nothing prevents the access
#_ by its is a valid variable name

g = sorted(globals())
for x in g:
    print(x)
