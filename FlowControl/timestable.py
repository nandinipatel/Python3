#Author: Nandini Patel
#Date: April 21, 2020
#Description: Nested for loops

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(i, j, i*j))
    print("-" * 20)