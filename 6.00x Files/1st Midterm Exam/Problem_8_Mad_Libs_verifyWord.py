def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[NOUN]':
        return userWord in listOfNouns
    elif madTemplate == '[VERB]':
        return userWord in listOfVerbs
    return False
