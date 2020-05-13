#Author: Nandini Patel
#Date: May 10, 2020
#Description: Understanding scopes, recursion, namespaces in Python

def fact(n):
    """ calculate n! iteratively!"""

    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *=f
    return result

def fact_rec(n):
    """ calculate n! recursively!"""

    if n <= 1:
        return 1
    else:
        return n * fact_rec(n-1)

def fib(n):
    """ F(n) = F(n-1) + F(n-2) """

    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2) 

def fib_itr(n):
    """ Run Fibonacci iteratively """

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0

        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

if __name__ == "__main__":
    for i in range(36):
        print(i, fib(i), fib_itr(i))