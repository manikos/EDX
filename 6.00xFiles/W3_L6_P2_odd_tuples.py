def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, only the odd elements of aTup 
    '''
    retTup=()
    for i in range(0,len(aTup),2):
        retTup+= (aTup[i],)
    return retTup
