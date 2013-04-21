import random

def pickUp():
    reds = 0
    x = (0.5, 0.4, 0.25)
    for i in range(3):
        if random.random() < x[i]:
            reds += 1
    print 'red balls=', reds
    if reds==3: return 
    return reds/3.0

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    total = 0
    for i in range(numTrials):
        total += pickUp()
    return total/numTrials
