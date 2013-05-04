import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global MAXRABBITPOP
    global CURRENTRABBITPOP
    rabits_list = range(CURRENTRABBITPOP)
    
    for rabit in rabits_list:
        if random.random() < 1 - (CURRENTRABBITPOP/float(MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    foxes_list = range(CURRENTFOXPOP)
    
    for fox in foxes_list:
        if CURRENTRABBITPOP > 10:
            if random.random() < (CURRENTRABBITPOP/float(MAXRABBITPOP)):
                CURRENTRABBITPOP -= 1
                if random.random() < 1/3.0:
                    CURRENTFOXPOP += 1
            else:
                if CURRENTFOXPOP > 10:
                    if random.random() < 10/100.0:
                        CURRENTFOXPOP -= 1
                    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []

    for i in range(numSteps):
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)

    return (rabbit_populations, fox_populations)

numSteps = 200
rabbit_populations, fox_populations = runSimulation(numSteps)
xVals = pylab.array(range(numSteps))
extX = pylab.array(range(numSteps*2))
pylab.plot(xVals, rabbit_populations, 'b.', label='Rabbit pop')
pylab.plot(xVals, fox_populations, 'r.', label='Fox pop')
pylab.grid(True)
coeffs_r = pylab.polyfit(xVals, rabbit_populations, 2)
coeffs_f = pylab.polyfit(xVals, fox_populations, 2)
y_rabbit_vals = pylab.polyval(coeffs_r, xVals)
y_fox_vals = pylab.polyval(coeffs_f, xVals)
pylab.plot(xVals, y_rabbit_vals, 'b', label='Order 2 rabit pop')
pylab.plot(xVals, y_fox_vals, 'r', label='Order 2 fox pop')
pylab.legend(loc='best')
pylab.title('Rabbits against foxes population')
pylab.xlabel('Time-step')
pylab.ylabel('Number of Rabbits and Foxes')
pylab.show()
