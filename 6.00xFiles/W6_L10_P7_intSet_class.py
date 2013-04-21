class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        """Returns a new intSet instance containing elements
        that appear in both sets (self and other)"""
        another=intSet()
        another.vals=[]
        for i in self.vals:
            if i in other.vals:
                another.vals.append(i)
        return another.__str__()

    def __len__(self):
        """Returns the number of elements in self instance"""
        counter=0
        for i in self.vals:
            counter+=1
        return counter

set1=intSet()
set2=intSet()

set1.insert(5)
set1.insert(6)
set1.insert(7)
set1.insert(8)
set1.insert(0)
set1.insert(-3)

set2.insert(4)
set2.insert(5)
set2.insert(6)
set2.insert(9)
set2.insert(0)
print 'set1=', set1, 'set2=', set2
set1.intersect(set2)
