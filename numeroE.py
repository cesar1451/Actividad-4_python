import os

def factorial(n):
    if(n == 0 or n == 1):
        n=1
    else:
        n = n * factorial(n-1)
    return n
