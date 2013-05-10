## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

## Find the sum of all the primes below two million.

def isPrime(n):
    from math import sqrt
    checkList=[]
    if n==1:
        return False
    for i in range(1,int(sqrt(n))):
        if n%(i+1) == 0:
            return False
    return True


def twoMillionSumPrimes():
    i = 2
    primes = 0

    while i < 2000000:
        if isPrime(i):
            primes += i
        i += 1

    return primes

twoMillionSumPrimes()
#ANSWER = 142913828922
