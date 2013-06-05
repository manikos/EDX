def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n<0: return False
    if n==0 or n%5==0 or n%8==0 or n%24==0: return True

    for a in range(n/5+1):
        for b in range(n/8+1):
            for c in range(n/24+1):
                guess = 5*a + 8*b + 24*c
                if guess==n:
                    return True
                elif guess>n:
                    break
    return False
