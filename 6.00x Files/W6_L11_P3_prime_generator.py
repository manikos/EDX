def genPrimes():
    '''returns the sequence of prime numbers on successive calls
    to its next() method: 2, 3, 5, 7, 11, ...'''
    number = 1
    while True:
        isPrime = True
        number += 1
        for i in range(2, int(number/2)+1):
            if number%i == 0:
                isPrime = False
                break
        if isPrime:
            yield number
