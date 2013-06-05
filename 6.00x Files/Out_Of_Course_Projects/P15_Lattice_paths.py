# Starting in the top left corner of a 22 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.

# How many such routes are there through a 2020 grid?

def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]

    # initialize wrapper function's cache.
    memf.cache = {} #function's attribute
    return memf

def paths(n, m):
    if n == 0 or m == 0:
        return 1
    return paths(n-1, m) + paths(n, m-1)

paths = memoize(paths)
print paths(20,20)

## ANSWER = 137846528820
