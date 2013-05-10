## The following iterative sequence is defined for the set of positive integers:

## n  n/2 (n is even)
## n  3n + 1 (n is odd)

## Using the rule above and starting with 13, we generate the following sequence:

##                 13  40  20  10  5  16  8  4  2  1
## It can be seen that this sequence (starting at 13 and finishing at 1)
## contains 10 terms. Although it has not been proved yet (Collatz Problem),
## it is thought that all starting numbers finish at 1.

## Which starting number, under one million, produces the longest chain?

## NOTE: Once the chain starts the terms are allowed to go above one million.

max_length = 0
for trial in xrange(1, 1000000):
    list_with_numbers = [trial]
    number = trial
    #print 'Before WHILE:', list_with_numbers
    while list_with_numbers[-1] != 1:
        if list_with_numbers[-1]%2 == 0:
            list_with_numbers.append(number/2)
            number = number/2
            #print 'IF:', list_with_numbers
        else:
            list_with_numbers.append((3*number+1))
            number = 3*number+1
            #print 'ELSE:', list_with_numbers
    if len(list_with_numbers) > max_length:
        max_length = len(list_with_numbers)
        ans = trial
    #print 'After WHILE', list_with_numbers

print ans


## ANSWER = 837799
