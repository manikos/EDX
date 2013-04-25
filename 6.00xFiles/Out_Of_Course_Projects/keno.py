#FINDS THE BEST NUMBER CHOICE (OUT OF 20) FOR MAXIMUM PROFIT PLAYING KENO
import random

def simpleKeno(numTrials):
    allNumbers = range(1,81)
    bingoList = [0.0]*20
    
    for i in range(numTrials):
        twentyNumbers = []
        userNumbers = []
        while len(twentyNumbers)<20:
            numberPC = random.choice(allNumbers)
            if numberPC not in twentyNumbers:
                twentyNumbers.append(numberPC)
        while len(userNumbers)<10:
            numberUser = random.choice(allNumbers)
            if numberUser not in userNumbers:
                userNumbers.append(numberUser)
        print sorted(twentyNumbers)
        print sorted(userNumbers)
        
