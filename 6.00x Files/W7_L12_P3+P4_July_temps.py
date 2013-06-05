def temperatures():
    inFile=open('julyTemps.txt', 'r', 0)
    highList, lowList = [], []
    for line in inFile:
        fields = line.split(' ')
        if len(fields)==3 and fields[0].isdigit():
            highList.append(int(fields[1]))
            lowList.append(int(fields[2]))
    return (lowList, highList)

def producePlot(lowTemps, highTemps):
    import pylab
    diffTemps=[highTemps[i]-lowTemps[i] for i in range(len(lowTemps))]
    pylab.plot(range(1,32), diffTemps)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
ret=temperatures()
producePlot(ret[0], ret[1])
