def iterPower(base,exp):
    result=1.0
    while exp>0:
        result*=base
        exp-=1
    return result
