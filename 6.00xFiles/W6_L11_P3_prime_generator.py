def genPrimes():
    '''returns the sequence of prime numbers on successive calls
    to its next() method: 2, 3, 5, 7, 11, ...'''
    n=2
    while True:
        checkList=[]
        for i in range(1,n-1):
            if n%(i+1)!=0:
                checkList.append(n%(i+1))
            else:
                checkList.append(0)
        if checkList.count(0)==0:
            yield n
        n+=1
