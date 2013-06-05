def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    storyList=story.split(' ')
    madLibsList=storyList[:]
    
    for i in range(len(storyList)):
        if storyList[i] in listOfAdjs:
            madLibsList[i] = '[ADJ]'
        elif storyList[i] in listOfNouns:
            madLibsList[i] = '[NOUN]'
        elif storyList[i] in listOfVerbs:
            madLibsList[i] = '[VERB]'

    madLibs=' '.join(madLibsList)
    return madLibs

##story = 'The ravenous zombies started attacking yesterday'
##listOfAdjs = ['ravenous']
##listOfNouns = ['zombies', 'humans', 'yesterday']
##listOfVerbs = ['attacking', 'attacks']
##print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = []
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = []
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
