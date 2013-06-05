animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals = { 'a': []}
animals['d'] = ['donkey', 'denver', 'dunlop']
animals['e'] = ['elepou']
animals['e'].append('eog')
animals['e'].append('eingo')
animals['e'].append('eonkey')
animals['e'].append('eog')
animals['b'].append('bingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    testValue=[]
    testKey=''
    for i in aDict:
        if len(aDict[i])>=len(testValue):
            testValue=aDict[i]
            testKey=i
    if testKey!='':
        return testKey
    else:
        return None
            
