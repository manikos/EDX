# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr)<2:
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[:-1])

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x)<1:
        return True
    elif len(x)>=1 and len(word)<1:
        return False
    elif word[0]!=x[0]:
        return x_ian(x,word[1:])
    elif word[0]==x[0]:
        return x_ian(x[1:],word[1:])

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength): #wrapper function
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    def insertNewlinesRec(text, lineLength, s, index): #recursive function
        if len(text)<1:   #Base case: Epeidi kathe fora temaxizw to text, an to text meinei keno
            return s      #return to s poy exei mazeytei me tis join methodous
        elif index==lineLength:   #An to index (metritis stin ousia)==orio poy prepei na mpei line feed
            if text[0]==' ':      #tote an to prwto stoixeio (panta doyleyw me to prwto stoixeio)=space
                index=1           #tote simainei oti prepei na mpei \n. Midenizw ton metriti mou
                #kai kanw concatenate to space + \n + recursive. Stin ousia kanw reset ta panta kai 3anakalw tin recursive function
                return s.join(text[0]) + s.join('\n') + insertNewlinesRec(text[1:],lineLength,s,index)
            else: #Edw einai oli i poustia. An omws meta to kampanaki (index=lineLength) synexizoun ta grammata (le3eis)
                  #tote synexizw na ektypwnw ALLA me orisma panta to index=lineLength gia na pigainei synexeia sto prwto elif kai kapote na vrei to space
                return s.join(text[0]) + insertNewlinesRec(text[1:],lineLength,s,lineLength)
        elif index<lineLength: # edw ousiastika einai to prwto elif poy ekteleitai kai apothikeyei ta grammata sto s me tin join
            return s.join(text[0]) + insertNewlinesRec(text[1:],lineLength,s,index+1)
    if text=='':
        return ''
    else:   #edw einai i klisi tis recursive function me orisma toy index=1 kai oxi miden giati o anthrwpos metraei apo to 1
        return insertNewlinesRec(text,lineLength,'',1)
