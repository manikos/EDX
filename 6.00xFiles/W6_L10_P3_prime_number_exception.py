def isPrime(n):
    '''returns True if the positive integer n is a prime number
    and False otherwise.
    The function raises a TypeError if n isn't an integer and
    a ValueError if n is an integer less than or equal to zero'''
    if type(n)!=int: raise TypeError
    if n<=0: raise ValueError
    checkList=[]
    if n==1:
        return False
    for i in range(1,n-1):
        if n%(i+1)!=0:
            checkList.append(n%(i+1))
        else:
            checkList.append(0)
    return checkList.count(0)==0
