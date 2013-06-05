def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    madLibsList = madLibsForm.split(' ')
    templateList = []
    
    for word in madLibsList:
        if word=='[ADJ]' or word=='[VERB]' or word=='[NOUN]':
            templateList.append(word)
    return templateList

madLibsForm='At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
generateTemplates(madLibsForm)
