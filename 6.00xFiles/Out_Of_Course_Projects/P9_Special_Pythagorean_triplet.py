## A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

##                  a^2 + b^2 = c^2
## For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

for a in range(1, 1000):
    for b in range(a, 1000):
        c = str((a**2+b**2)**0.5)
        if c[-1] == '0':
            c = int(float(c))
            if a+b+c == 1000:
                print str(a*b*c)

## ANSWER = 31875000
