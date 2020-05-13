with open("original.txt", 'a') as jabberwocky:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=jabberwocky)
        print("-"*20, file=jabberwocky)