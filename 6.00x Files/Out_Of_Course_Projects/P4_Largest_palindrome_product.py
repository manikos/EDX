## A palindromic number reads the same both ways. The largest palindrome made
## from the product of two 2-digit numbers is 9009 = 91  99.

## Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(test):
    '''
    test: a string
    
    returns: True if test is palindrome, False otherwise.
    '''
    if len(test) % 2 != 0:
        return False
    if len(test)< 2:
        return True
    if test[0] == test[-1]:
        #print 'Sygkrisi: ' + test[0]+ '=' + test[-1]
        return isPalindrome(test[1:-1])
    else:
        return False

def palindomicNumber():
    upperlimit = 999
    downlimit = 900
    while True:
        for i in xrange(upperlimit, downlimit, -1):
            for j in xrange(upperlimit, downlimit, -1):
                if isPalindrome(str(i*j)):
                    return i*j
        upperlimit -= 100
        downlimit -= 100

## ANSWER = 906609
        
                
    
