import os

def factorial(n):
    if(n == 0 or n == 1):
        n=1
    else:
        n = n * factorial(n-1)
    return n

limite = 300
n = 0
e = 0

for n in range(0,limite):
    e += 1 / factorial(n)
    n = n + 1

print("El número e = ", e)
