## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
## see that the 6th prime is 13. What is the 10,001st prime number?

def isPrime(n):
    from math import sqrt
    checkList=[]
    if n==1:
        return False
    for i in range(1,int(sqrt(n))):
        if n%(i+1) == 0:
            return False
    return True


def ThousandPrime():
    countPrime = 0
    i = 2

    while countPrime < 10001:
        if isPrime(i):
            countPrime += 1
            prime = i
        i += 1

    return prime

#ANSWER = 104743
