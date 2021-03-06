## Each new term in the Fibonacci sequence is generated by adding the previous
## two terms. By starting with 1 and 2, the first 10 terms will be:
##
##                1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
## By considering the terms in the Fibonacci sequence whose values do not
## exceed four million, find the sum of the even-valued terms.

def fib(n):
    '''assumes n=int>=0
    Returns Fibonacci of n'''
    if n==0 or n==1:
       return 1
    else:
        return fib(n-1)+fib(n-2)

def findSumFib():
    evenFibNumbers = []
    temp, st = 1, 1
    while st < 4000000:
        if st%2 == 0:
            evenFibNumbers.append(st)
        st = fib(temp)
        temp += 1
    return sum(evenFibNumbers)

#ANSWER IS: 4613732
