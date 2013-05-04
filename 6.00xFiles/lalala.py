import math
import string
import time
import datetime
import sys
import copy
import random
import pylab

####ASSERTION
##while True:
##    x=int(raw_input('Insert a number [0,20]: '))
##    assert x<=20 and x>=0, 'You did not enter a number between 0 and 20'
##

####EXCEPTIONS (HANDLING)
##string='hello'
##number=34
##lista=[3, 4, 'hello']
##def FError(string, number, lista):
##    print '**Understanding Exceptions**\n'
##    try:
##        print 'Will now execute division by zero'
##        divE=number/0
##        print 'Will now concatenate wrong values'
##        stE=string+number
##        print 'Will now index a list out of range '
##        lsE=lista[6]
##    except ZeroDivisionError as e:
##        print 'Handled the error: Division by zero'
##        return lista
##    except TypeError:
##        print 'Handled the error: Cannot concatenate ', string, ' with ', number
##    except IndexError:
##        print 'Handled the error: List index is out of range'
##    else:
##        print 'No errors: OLA OK. No problem'
##    finally:
##        print 'FINALLY will always be printed'
##    print 'Exiting this looooong function'
##    
##j=FError(string, number, lista)
##print j,

####INNER OUTTER FUNCTION DIFFERENCE
##def outer(x,y):
##    def inner(x,y):
##        y=x+1
##        return y
##    y=y
##    return y
##

####GIVVEN A STRING, COMPOSES A WORD USING EACH LETTER ONLY ONCE
##def findAll (wordList, lstr):
##    dct={}
##    validList=[]
##
##    for i in lstr:
##        dct[i]=1
##
##    for word in wordList:
##        count=0
##        for i in word:
##            if i in dct.keys() and dct[i]==1:
##                count+=1
##        if count==len(word):
##            for i in word:
##                dct[i]=0
##            validList.append(word)
##    return validList
##
##wordList=['god', 'air', 'the', 'hello', 'mud', 'then', 'star', 'lips', 'war']
##lstr='gdotehlisp'

####STRING GAMES
##def isWordIn(word, text):
##        """text: a string
##        returns: Boolean whether word is in string"""
##        tempText=text.lower()
##        tempWord=word.lower()
##        for letter in tempText:
##            if letter in string.punctuation:
##                tempText=tempText.replace(letter,' ')
##        listOfWords=tempText.split()
##        return tempWord in listOfWords
##
##word='sOfT'
##text=['Soft\'s the new pink!',
##      'Koala bears are soft and cuddly.',
##      'I prefer pillows that are soft.',
##      'Microsoft recently released the Preview.',
##      'Downey makes my clothes the softest they can be!',
##      'softex is softs\'s my unsofted sotf \'softer']
##for i in text:
##    print isWordIn(word,i)


####BINARY SEARCH IN A SORTED LIST
##def search(L, e):
##    def bSearch(L, e, low, high):
##        if high == low: # i.e. list of lenght 1
##            print 'A. the L[low] = ',L[low]
##            return L[low] == e
##        mid = low + int((high - low)/2)
##        print 'B. mid= %s and L[mid]= %d'%(mid, L[mid])
##        if L[mid] == e:
##            print 'E. i found it ',L[mid]
##            return True
##        if L[mid] > e:
##            print 'C. Same low=%d, New high=%d '%(L[low], L[mid - 1])
##            return bSearch(L, e, low, mid - 1)
##        else:
##            print 'D. New low=%d, Same high=%d '%(L[mid + 1], L[high])
##            return bSearch(L, e, mid + 1, high)
##    if len(L) == 0:
##        return False
##    else:
##        print 'X. initial max = len(L)-1 =',len(L)-1
##        return bSearch(L, e, 0, len(L) - 1) #low = 0 , high = Len(L)-1
##
##
##L = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
##print 'len(l) =',len(L),'\n'
##print L
##print ' |  |  |  |   |    |   |    |    |    |'
##print '[0  1  2  3   4    5   6    7    8    9]\n'
##e = 16
##print 'Looking for value ***%d***\n'  %e
##print search(L, e) 

####RECURSION EXAMPLE
##def isPalPrint(s, indent='  '):
##    print indent, 'isPalPrint called with: ', repr(s)
##    if len(s)<=1:
##        print indent, 'About to return True from Base Case'
##        return True
##    else:
##        ans= s[0]==s[-1] and isPalPrint(s[1:-1],indent+indent)
##        print indent, 'About to return ', ans, 'for: ', s
##        return ans
##    
##def isPalindromePrint(s):
##    return isPalPrint(s)
##
##isPalindromePrint('guttag')

####UNDERSTANDING BREAK STATEMENT
##check=20
##while True:
##    print 'check[OUTTER]=%d' %check
##    if check==5:
##        print 'Will now break out outter WHILE'
##        break
##    while True:
##        check-=1
##        print 'check[INNER]=%d' %check
##        if check==5:
##            print 'Will now break out inner WHILE'
##            break

####CLASSES, ATTRIBUTES AND METHODS
##class Point(object):
##    pass
##class Rectangle(object):
##    pass
##def distance(pointObj1,pointObj2):
##    dx=pointObj2.x - pointObj1.x
##    dy=pointObj2.y - pointObj1.y
##    dsquared=dx**2+dy**2
##    result=math.sqrt(dsquared)
##    return result
##def findCenter(rectObj):
##    p=Point() #to instance p einai local. Gia xrisi mono mesa stin findCenter
##    p.x=rectObj.corner.x + rectObj.width/2.0
##    p.y=rectObj.corner.y - rectObj.height/2.0
##    return p #vevaia edw to epistrefw kai mporw na to xrhsimopoihsw global
##def samePoint(p1,p2):
##    return p1.x==p2.x and p1.y==p2.y
##def printPoint(p):
##    print '('+str(p.x)+', '+str(p.y)+')'
##
##dot1,dot2=Point(),Point()
##dot1.x, dot1.y = 5, 6
##dot2.x, dot2.y = 9, 10
##
##box=Rectangle()
##box.width=100.0
##box.height=200.0
##box.corner=Point() #box.corner einai instance ths Point(),
###enw to box paramenei instance ths Rectangle()
##box.corner.x=0.0
##box.corner.y=0.0

####IMPROVED FIND FUNCTION
##def find(words, ch, start=0, stop=None):
##    index=start
##    if stop==None: stop=len(words)
##    while index < stop:
##        if words[index] == ch:
##            return index
##        index+=1
##    return -1

####CLASS INHERITANCE #1
##class A(object):
##    def __init__(self):
##        self.a = 1
##    def x(self):
##        print "A.x"
##    def y(self):
##        print "A.y"
##    def z(self):
##        print "A.z"
##
##class B(A):
##    def __init__(self):
##        A.__init__(self)
##        self.a = 2
##        self.b = 3
##    def y(self):
##        print "B.y"
##    def z(self):
##        print "B.z"
##
##class C(object):
##    def __init__(self):
##        self.a = 4
##        self.c = 5
##    def y(self):
##        print "C.y"
##    def z(self):
##        print "C.z"
##
##class D(C, B):
##    def __init__(self):
##        C.__init__(self)
##        B.__init__(self)
##        self.d = 6
##    def z(self):
##        print "D.z"

####CLASS INHERITANCE #2
##class Alpha(object):
##    def __init__(self, n):
##        self.n=n
##        self.y=n*2
##
##    def isok(self, word):
##        s= "ALPHA: "+ str(self.y) + "printed by ALPHA" + str(word)
##        return s
##
##class Vita(Alpha):
##    def __init__(self, n):
##        Alpha.__init__(self, n)
##
##    def isisok(self, word):
##        return self.isok(word)

####CLASS DECORATORS AND PROPERTY
##class Color(object):
##    def __init__(self, rgb_value, name):
##        self.rgb_value = rgb_value
##        self.name = name
##        
##class Color0(object):
##    def __init__(self, rgb_value, name):
##        self.rgb_value = rgb_value
##        self._name = name # change name attribute to semi-private _name
##   
##    def _set_name(self, name): # add semi-private method _set_name to set name
##        self._name = name
##   
##    def _get_name(self): # add semi-private method _get_name to get name
##        return self._name
##
##class Color1(object):
##    def __init__(self, rgb_value, name):
##        self.rgb_value = rgb_value
##        self._name = name # change name attribute to semi-private _name
##   
##    def _set_name(self, name): # add semi-private method _set_name to set name
##        if name == "":
##            print 'where is the name?'
##        self._name = name
##   
##    def _get_name(self): # add semi-private method _get_name to get name
##        return self._name
##   
##    name = property(_get_name, _set_name)   # `name` is the attribute we want to get/set, etc i.e print c1.`name` / c1.`name` = value
##                                            # creates a new attribute on the Color class called name , which now *replaces the previous
##                                            # name attribute*. It sets this attribute to be a *property*, which calls the two methods
##                                            # we just created *whenever the property is accessed or changed*.
##                                            # This new version of the Color class can be used exactly the same way as the previous version, yet it now
##                                            # does validation when we set the name (we do not need to change access method!!!)
##
##class Names(object):
##    def __init__(self, fullName):
##        self._firstName = str(fullName.split(' ')[0])
##        self._surName = str(fullName.split(' ')[1]) # change name attribute to semi-private _name
##   
##    @property # this is getter by default. It's equal to color = property(color).  You have to define getter first, else error !!!
##    def name(self):
##        s='Your name is ' + self._firstName + ' ' + self._surName
##        return s
##   
##    @name.setter # this is setter for var name
##    def name(self, fullName): # the  getter function should be called whatever we want to set, e.g we want to set c2.`name` attribute, thus def `name`
##        if fullName == '':
##            print "You haven't provide any name motherfucker"
##            return
##        self._firstName = str(fullName.split(' ')[0])
##        self._surName = str(fullName.split(' ')[1])

####GENERATORS
##def generator1():
##    if True:
##        yield 1 
##
##def generator2():
##    if False:   
##        yield 1
##
##g1 = generator1()
##g2 = generator2()
##
##print type(g1)
##print type(g2)
##print g1.next()
##print g2.next()

####ALTERNATIVE WAY TO PLOT 2 DIAGRAMS UNDER THE SAME X-AXIS RANGE
##import random, pylab
##
##x = [random.random() for i in xrange(1000)]
##y = [2*random.random() for i in xrange(1000)]
##
### subplot sharing the same axis (http://matplotlib.org/examples/pylab_examples/subplots_demo.html)
##f, axarr = pylab.subplots(2, sharex=True)
##
##print f
##print axarr
##
##axarr[0].plot(x, y , 'bo')
##axarr[1].hist(y, bins=100)
##pylab.show()
##
###subplot not share the same axis (http://matplotlib.org/examples/pylab_examples/subplot_demo.html)
##pylab.subplot(211)
##pylab.plot(x, y)
##pylab.subplot(212)
##pylab.hist(y, bins=100)
##pylab.show()

####PYLAB SUM OF 2 DISTRIBUTIONS GIVES UNIFORM DISTRIBUTION
##vals1, vals2, vals = [], [], []
##for i in range(1000):
##    num1=random.choice(range(1,50))
##    num2=random.choice(range(1,50))
##    vals1.append(num1)
##    vals2.append(num2)
##    vals.append(vals1[i]+vals2[i])
###print 'len(vals1)=', len(vals1), 'len(vals2)=', len(vals2), 'len(vals)=', len(vals)
###print sorted(vals1), '\n', sorted(vals2), '\n', sorted(vals)
###print (vals1), '\n', (vals2), '\n', (vals)#, '\n', sorted(vals)
##pylab.subplot(3,1,1)
##pylab.plot(range(1000), vals1, 'bo')
##pylab.subplot(3,1,2)
##pylab.plot(range(1000), vals2, 'ro')
##pylab.subplot(3,1,3)
##pylab.plot(range(1000), vals, 'mo')
##pylab.show()

####POWER-SET. COMBINATIONS OF N-ELEMENTS TO FIT IN 1 BAG
##def myPowerSet(iterative):
##    """
##    Given an iterative object (list, tuple, string), computes all
##    the possible subsets (combinations) that can be formed in order
##    to fit in a single bag. That is, an element can be either
##    inside the bag (value=1) or not (value=0).
##
##    yields: a list which contains the subset
##    """
##    length = len(iterative)
##    combinations = 2**length
##    for combo in range(combinations):
##        bag = []
##        binary = bin(combo)[2:]
##        if len(binary) != length:
##               binary = '0'* (length - len(binary)) + binary
##        for test in range(len(binary)): #binary is in form '010', or '1101' etc.
##            if binary[test]=='1':
##                bag.append(iterative[test])
##        yield bag

####UNDERSTANDING POLYFIT AND POLYVAL METHODS
##x = [1, 1.5, 2, 3, 5, 5.5, 7, 9, 10]
##y = [2, 4, 7, 3, 1, 5, 8, 9, 6]
##new_x = pylab.linspace(1, 10)
##coeffs1 = pylab.polyfit(x, y, 1)
##coeffs3 = pylab.polyfit(x, y, 3)
##coeffs5 = pylab.polyfit(x, y, 5)
##new_y1 = pylab.polyval(coeffs1, new_x)
##new_y3 = pylab.polyval(coeffs3, new_x)
##new_y5 = pylab.polyval(coeffs5, new_x)
##pylab.plot(x, y, 'rx', label="Orig. Data")
##pylab.plot(new_x, new_y1, 'k', label="Order 1")
##pylab.plot(new_x, new_y3, 'b', label="Order 3")
##pylab.plot(new_x, new_y5, 'g', label="Order 5")
##pylab.legend(loc='best')
##pylab.title('Curve Fits')
##pylab.xlabel('x-axis')
##pylab.ylabel('y-axis')
##pylab.show()

