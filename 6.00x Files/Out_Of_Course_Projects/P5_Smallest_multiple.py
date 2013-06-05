## 2520 is the smallest number that can be divided by each of the numbers from
## 1 to 10 without any remainder.

## What is the smallest positive number that is evenly divisible by all of the
## numbers from 1 to 20?

number = 10

while True:
    test = 0
    for divisor in range(2, 21):
        if number%divisor != 0:
            break
        else:
            test += 1
    if test ==19:
        break
    number += 10
    
print number

## ATERNATIVE - FASTER WAY OF FINDIND ALL DIVISORS OF NUMBER n
##n=90
##print set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

## ANSWER = 232792560
