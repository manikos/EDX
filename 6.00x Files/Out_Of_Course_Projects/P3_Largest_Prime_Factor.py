## The prime factors of 13195 are 5, 7, 13 and 29.
## What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def weirdPrime(n):
    number = None
    i=1
    while i < sqrt(n-1):
        if n%(i+1) == 0 and isPrime(i+1):
            number = i+1
        i += 1
    return number

def isPrime(n):
    '''returns True if the positive integer n is a prime number
    and False otherwise.
    The function raises a TypeError if n isn't an integer and
    a ValueError if n is an integer less than or equal to zero'''
    i=1
    while i < sqrt(n-1):
        if n%(i+1) == 0:
            return False
        i += 1
    return True

#ANSWER = 6857
