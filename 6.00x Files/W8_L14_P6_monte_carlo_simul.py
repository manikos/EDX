import random

def pickUp():
    bucket = ['r', 'r', 'r', 'g', 'g', 'g']
    reds, greens = 0, 0
    for turn in range(3):
        ball = random.choice( bucket )
        if ball == 'r':
            reds += 1
        else:
            greens +=1
        bucket.remove(ball)
    if reds == 3 or greens ==3:
        return True
    return False

    
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    total = 0.0
    for i in range(numTrials):
        if pickUp():
            total += 1
    return total/numTrials
