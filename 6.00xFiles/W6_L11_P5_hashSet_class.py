class hashSet(object):
    """Implements a simple hashed set"""
    def __init__(self, numBuckets):
        """numBuckets: int. The number of buckets this hash set will have.
        Raises ValueError if this value is not an integer, or is not greater than zero.
        Sets up an empty hash set with numBuckets number of buckets."""
        if type(numBuckets)!=int or numBuckets<=0: raise ValueError
        self.numBuckets=numBuckets
        self.hashList=[]
        for i in range(numBuckets):
            self.hashList.append([])

    def hashValue(self, e):
        """e: an integer
        returns: a hash value for e, which is simply e modulo the number
        of buckets in this hash set.
        Raises ValueError if e is not an integer."""
        if type(e)!=int: raise ValueError
        return e%self.numBuckets

    def member(self, e):
        """e: an integer
        returns: True if e is in self, False otherwise.
        Raises ValueError if e is not an integer"""
        if type(e)!=int: raise ValueError
        return e in self.hashList[self.hashValue(e)]

    def insert(self, e):
        """e: an integer
        Inserts e into the appropriate bucket.
        Raises ValueError if e is not an integer"""
        if type(e)!=int: raise ValueError
        if self.hashList[self.hashValue(e)].count(e)==0:
            self.hashList[self.hashValue(e)].append(e)

    def remove(self, e):
        """e: an integer
        Removes e from self
        Raises ValueError if e in not in self or
        if e is not an integer"""
        if type(e)!=int or not self.member(e): raise ValueError
        self.hashList[self.hashValue(e)].remove(e)

    def getNumBuckets(self):
        """returns: total number of buckets"""
        return self.numBuckets

    def __str__(self):
        im=''
        for e in range(len(self.hashList)):
            self.hashList[e].sort()
            im+='Bucket No.' + str(e) + ': ' + str(self.hashList[e]) + '\n'
        return im

h=hashSet(5)

for i in range(0,200,6):
    h.insert(i)
