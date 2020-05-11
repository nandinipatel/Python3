#Author: Nandini Patel
#Date: April 22, 2020
#Description: Learning tuples

#tuples cannot be changed; are immutable
t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

#passing a tupple, enclose it in parantheses
print()

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (
        (1, "Pulling the Ruge"), (2, "Pscycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)