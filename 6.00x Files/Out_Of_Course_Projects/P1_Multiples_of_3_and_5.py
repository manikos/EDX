## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.

def mult_3_and_5(maxNum=1000):
    numbers = []
    for i in range(maxNum):
        if i%3 == 0 or i%5 == 0:
            numbers.append(i)
    return sum(numbers)
    
##ANSWER = 233168
