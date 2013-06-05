##DETERMINISTIC
import random
def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    return 10



##STOHASTIC
import random
def stochasticNumber():
    '''
    Stochastically generates an even number between 9 and 21
    '''
    return random.choice(range(10,21,2))
