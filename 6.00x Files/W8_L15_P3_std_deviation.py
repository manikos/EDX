def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L)<1: return float('NaN')

    totalLength = 0.0
    for s in L:
        totalLength += len(s)
    meanLength = totalLength/len(L)
    suma = 0.0
    for s in L:
        suma += (len(s)-meanLength )**2
    return ( suma/len(L) )**0.5
