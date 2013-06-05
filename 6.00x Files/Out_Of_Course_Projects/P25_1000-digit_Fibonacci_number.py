## PROBLEM 25

## The Fibonacci sequence is defined by the recurrence relation:

## Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
## Hence the first 12 terms will be:

## F1 = 1
## F2 = 1
## F3 = 2
## F4 = 3
## F5 = 5
## F6 = 8
## F7 = 13
## F8 = 21
## F9 = 34
## F10 = 55
## F11 = 89
## F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?

def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(x):
        if x not in memf.cache:
            memf.cache[x] = f(x)
        return memf.cache[x]

    # initialize wrapper function's cache.
    memf.cache = {} #function's attribute
    return memf


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)
i = 1
while len(str(fib(i))) < 1000:
    i += 1

print i+1


## ANSWER = 4782
