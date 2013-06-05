import string
import pylab

WORDLIST_FILENAME = "words.txt"

print "Loading word list from file..."
# inFile: file
inFile = open(WORDLIST_FILENAME, 'r', 0)
# line: string
line = inFile.readline()
# wordlist: list of strings
wordList = string.split(line)
print "  ", len(wordList), "words loaded."

letterOccurrence = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,\
                    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,\
                    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,\
                    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,\
                    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

#Fill in the dictionary with occurrences of each letter
for word in wordList:
    for letter in word:
        letterOccurrence[letter] += 1
#Due to arbitrary presentation of dictionary, a list [ ( , ) ] is used instead
listForPlot = []
for c in letterOccurrence.keys():
    listForPlot.append( (c, letterOccurrence[c]) )
listForPlot.sort()
occurrences = []
for tup in listForPlot:
    occurrences.append(tup[1])

#Vathmonomisi of X axis
N=26
xAxis = pylab.arange(N)
xTicks = [s for s in string.lowercase]

pylab.bar(xAxis, occurrences, width=0.8)
pylab.grid(True)
pylab.title('Letter occurrences of 55900 words in word.txt file')
pylab.ylabel('Occurrence (Times appeared)')
pylab.xlabel('Letters')
pylab.xticks(xAxis+0.8/2, xTicks)
pylab.show()
