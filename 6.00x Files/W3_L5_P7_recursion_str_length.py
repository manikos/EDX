def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    ans=1
    if aStr=='':
        return ans-1
    return ans+lenRecur(aStr[1:])
