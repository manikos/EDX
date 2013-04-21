animals = {'a':['aardvark'], 'b':['baboon'], 'c':['coati']}

animals['d']=['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    counter=0
    for i in aDict:
        for j in aDict[i]:
            counter+=1
    return counter
