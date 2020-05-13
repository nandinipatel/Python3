#Author: Nandini Patel
#Date: May 4, 2020
#Description: Write from a text file

# cities = ["Brampton", "Mississauga", "Etobicoke"]

# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []

# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))

# print(cities)
# for city in cities:
#     print(city)

#the following content will be written as a tupple but will be string
#it cannot be read back as a tupple
# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psyco"))

# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)