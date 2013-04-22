# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *


## ***START OF HELPER FUNCTIONS FOR PROBLEM #1, CREATED BY ME***

def simulationDelayed300(numTrials, numViruses=100, maxPop=1000,
                         maxBirthProb=0.1, clearProb=0.05,
                         resistances={'guttagonol': False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicine (guttagonol) delays to be administered (to the patient)
    for 300 time steps. That is, the patient lives with the virus for 300
    time steps and then the medicine is given for an additional 150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 450
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==300:
                patient.addPrescription('guttagonol')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationDelayed150(numTrials, numViruses=100, maxPop=1000,
                         maxBirthProb=0.1, clearProb=0.05,
                         resistances={'guttagonol': False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicine (guttagonol) delays to be administered (to the patient)
    for 150 time steps. That is, the patient lives with the virus for 150
    time steps and then the medicine is given for an additional 150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 300
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==150:
                patient.addPrescription('guttagonol')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationDelayed75(numTrials, numViruses=100, maxPop=1000,
                         maxBirthProb=0.1, clearProb=0.05,
                         resistances={'guttagonol': False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicine (guttagonol) delays to be administered (to the patient)
    for 75 time steps. That is, the patient lives with the virus for 75
    time steps and then the medicine is given for an additional 150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 225
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==75:
                patient.addPrescription('guttagonol')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationDelayed0(numTrials, numViruses=100, maxPop=1000,
                         maxBirthProb=0.1, clearProb=0.05,
                         resistances={'guttagonol': False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicine (guttagonol) delays to be administered (to the patient)
    for 0 time steps. That is, the patient lives with the virus for 0
    time steps and then the medicine is given for an additional 150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 150
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
                patient.addPrescription('guttagonol')
                trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop

##***END OF HELPER FUNCTIONS FOR PROBLEM #1, CREATED BY ME***

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.
    
    numTrials: number of simulation runs to execute (an integer)
    returns: 4 lists containing results from different number of trials
    """

    print "Simulating 300 time steps before administering guttagonol..."
    delayed300List = simulationDelayed300(numTrials)
    print "FINISHED #1--- delayed300List=", sorted(delayed300List)
    
    print "Simulating 150 time steps before administering guttagonol..."
    delayed150List = simulationDelayed150(numTrials)
    print "FINISHED #2--- delayed150List=", sorted(delayed150List)
    
    print "Simulating 75 time steps before administering guttagonol..."
    delayed75List = simulationDelayed75(numTrials)
    print "FINISHED #3--- delayed75List=", sorted(delayed75List)
    
    print "Simulating 0 time steps before administering guttagonol..."
    delayed0List = simulationDelayed0(numTrials)
    print "FINISHED #4--- delayed0List=", sorted(delayed0List)

    return delayed300List, delayed150List, delayed75List, delayed0List


def plotSimulationDelayedTreatment(numTrials=100):
    """
    Plots 4 histograms (one for each of the above returned delayedXLists)

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation). In detail, the x-axis of the histogram is the final total
    virus population values while the y-axis of the histogram is the number
    of trials belonging to each histogram bin.
    """
    ##Uncomment next line for Problem 1 to simulate
    #fin300List, fin150List, fin75List, fin0List = simulationDelayedTreatment(numTrials)

    ##Uncomment next line for Problem 2 to simulate
    fin300List, fin150List, fin75List, fin0List = simulationTwoDrugsDelayedTreatment(numTrials)

    pylab.figure()
    xAxisLabel = 'Virus population'
    yAxisLabel = 'Number of trials'

    #Plot the upper left histogram
    pylab.subplot(2,2,1)
    pylab.hist(fin300List, bins=numTrials, cumulative=True)
    pylab.xlim(0,600)
    pylab.grid(True)
    pylab.title('Virus population - 300 timesteps delay of drug')
    pylab.xlabel(xAxisLabel)
    pylab.ylabel(yAxisLabel)
    #Plot the upper right histogram
    pylab.subplot(2,2,2)
    pylab.hist(fin150List, bins=numTrials, cumulative=True)
    pylab.xlim(0,600)
    pylab.grid(True)
    pylab.title('Virus population - 150 timesteps delay of drug')
    pylab.xlabel(xAxisLabel)
    pylab.ylabel(yAxisLabel)
    #Plot the bottom left histogram
    pylab.subplot(2,2,3)
    pylab.hist(fin75List, bins=numTrials, cumulative=True)
    pylab.xlim(0,600)
    pylab.grid(True)
    pylab.title('Virus population - 75 timesteps delay of drug')
    pylab.xlabel(xAxisLabel)
    pylab.ylabel(yAxisLabel)
    #Plot the bottom right histogram
    pylab.subplot(2,2,4)
    pylab.hist(fin0List, bins=numTrials, cumulative=True)
    ##Uncomment next line for problem #1
    #pylab.xlim(0,2)
    ##Uncomment net line for problem #2
    pylab.xlim(0,600)
    pylab.grid(True)
    pylab.title('Virus population - No delay of drug')
    pylab.xlabel(xAxisLabel)
    pylab.ylabel(yAxisLabel)
    pylab.show()


#
# PROBLEM 2
#

##***START OF HELPER FUNCTIONS FOR PROBLEM #2, CREATED BY ME***

def simulationCocktails300(numTrials, numViruses=100, maxPop=1000,
                           maxBirthProb=0.1, clearProb=0.05,
                           resistances={'guttagonol': False, 'grimpex':False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicines (guttagonol and grimpex) delays to be administered (to the patient).
    That is, 150 timesteps-->guttagonol-->300 timesteps-->grimpex-->150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 600
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==150:
                patient.addPrescription('guttagonol')
            if timeStep==450:
                patient.addPrescription('grimpex')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationCocktails150(numTrials, numViruses=100, maxPop=1000,
                           maxBirthProb=0.1, clearProb=0.05,
                           resistances={'guttagonol': False, 'grimpex':False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicines (guttagonol and grimpex) delays to be administered (to the patient).
    That is, 150 timesteps-->guttagonol-->150 timesteps-->grimpex-->150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 450
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==150:
                patient.addPrescription('guttagonol')
            if timeStep==300:
                patient.addPrescription('grimpex')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationCocktails75(numTrials, numViruses=100, maxPop=1000,
                          maxBirthProb=0.1, clearProb=0.05,
                          resistances={'guttagonol': False, 'grimpex':False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicines (guttagonol and grimpex) delays to be administered (to the patient).
    That is, 150 timesteps-->guttagonol-->75 timesteps-->grimpex-->150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 375
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==150:
                patient.addPrescription('guttagonol')
            if timeStep==225:
                patient.addPrescription('grimpex')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop


def simulationCocktails0(numTrials, numViruses=100, maxPop=1000,
                         maxBirthProb=0.1, clearProb=0.05,
                         resistances={'guttagonol': False, 'grimpex':False}, mutProb=0.005):
    """
    Runs the simulation of a virus growth in a patient where the
    medicines (guttagonol and grimpex) delays to be administered (to the patient).
    That is, 150 timesteps-->guttagonol-->0 timesteps-->grimpex-->150 timesteps.

    returns: The FINAL viruses populations for each numTrial(list)
    """
    time_steps = 300
    totalPop = []
    
    for trial in range(numTrials):
        #Instantiate the Resistant Viruses first, TreatedPatient second
        viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses) ]
        patient = TreatedPatient(viruses, maxPop)
        for timeStep in range(time_steps):
            if timeStep==150:
                patient.addPrescription('guttagonol')
                patient.addPrescription('grimpex')
            trialPop = patient.update()
        totalPop.append(trialPop)

    return totalPop

##***END OF HELPER FUNCTIONS FOR PROBLEM #2, CREATED BY ME***

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    returns: 4 lists containing results from different number of trials
    """
    print "Simulating 300 time steps before administering guttagonol and grimpex..."
    delayed300List = simulationCocktails300(numTrials)
    print "FINISHED #1--- delayed300List=", sorted(delayed300List)
    
    print "Simulating 150 time steps before administering guttagonol and grimpex..."
    delayed150List = simulationCocktails150(numTrials)
    print "FINISHED #2--- delayed150List=", sorted(delayed150List)
    
    print "Simulating 75 time steps before administering guttagonol and grimpex..."
    delayed75List = simulationCocktails75(numTrials)
    print "FINISHED #3--- delayed75List=", sorted(delayed75List)
    
    print "Simulating 0 time steps before administering guttagonol and grimpex..."
    delayed0List = simulationCocktails0(numTrials)
    print "FINISHED #4--- delayed0List=", sorted(delayed0List)

    return delayed300List, delayed150List, delayed75List, delayed0List
