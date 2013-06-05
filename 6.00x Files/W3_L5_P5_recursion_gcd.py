def gcdRecur(a,b):
    if b==0:
        return a
    elif max(a,b)%min(a,b)==0:
        return min(a,b)
    return gcdRecur(min(a,b),max(a,b)%min(a,b))
