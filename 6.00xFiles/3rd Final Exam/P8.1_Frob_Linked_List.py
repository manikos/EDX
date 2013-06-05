class Frob(object):
    linked_list = []
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
        Frob.linked_list.append(self)
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def pList():
    frobs = sorted(Frob.linked_list, key=Frob.myName)
    print 'SORTED=', [f.myName() for f in frobs]
    print '\nGoing forward the list'
    print frobs[0].myName(), '->',
    for elem in frobs[:-1]:
        print elem.getAfter().myName(), '->',
    print '\n------------------------------------'
    print 'Going backward the list'
    print frobs[-1].myName(), '->',
    for elem in range(len(frobs)-1, 0, -1):
        print frobs[elem].getBefore().myName(), '->',

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    flag = False
    if newFrob.myName() > atMe.myName():
        while newFrob.myName() > atMe.myName():
            if atMe.getAfter() is None: # insert at the right edge
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
                flag = True
                break
            atMe = atMe.getAfter()
        if not flag:
            newFrob.setAfter(atMe)
            newFrob.setBefore(atMe.getBefore())
            atMe.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
        
    elif newFrob.myName() < atMe.myName():
        while newFrob.myName() < atMe.myName():
            if atMe.getBefore() is None: #insert at the left edge
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
                flag = True
                break
            atMe = atMe.getBefore()
        if not flag:
            newFrob.setAfter(atMe.getAfter())
            newFrob.setBefore(atMe)
            atMe.getAfter().setBefore(newFrob)

            atMe.setAfter(newFrob)
    else:
        if atMe.getAfter() is None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getBefore() is None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            newFrob.setAfter(atMe.getAfter())
            newFrob.setBefore(atMe)
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
