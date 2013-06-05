# -*- coding: utf-8 -*-

def temperatures():
    inFile=open('julyTemps.txt', 'r', 0)
    highList, lowList = [], []
    for line in inFile:
        fields = line.split(' ')
        if len(fields)==3 and fields[0].isdigit():
            highList.append( (int(fields[1])-32)*(5/9.0) )
            lowList.append( (int(fields[2])-32)*(5/9.0) )
    return (lowList, highList)

def producePlot(lowTemps, highTemps):
    import pylab
    #diffTemps=[highTemps[i]-lowTemps[i] for i in range(len(lowTemps))]
    N1 = range(1,32)
    N2 = [i+0.4 for i in range(1,32)]
    pylab.bar(N1, highTemps, width=0.4, color='r', align='center')
    pylab.bar(N2, lowTemps, width=0.4, color='b', align='center')
    pylab.title("Max and min Temperatures in Boston (July 2012)")
    pylab.xlabel('Day')
    pylab.xticks(range(1,32), rotation=70)
    pylab.ylabel('Temperature (' + unichr(176) + 'C)')
    pylab.show()
ret=temperatures()
producePlot(ret[0], ret[1])
