# -*- coding: utf-8 -*-

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
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

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked
    list that atMe is a part of.    
    """
    forbs_list = []
    me, newF = atMe.myName().lower(), newFrob.myName().lower()
    print me, newF, newF > me, newF < me
    if newF > me:
        while newF > me:
            me = (atMe.getAfter()).myName().lower()
            atMe = atMe.getAfter()
        newFrob.setAfter(atMe)
        newFrob.setBefore(atMe.getBefore())
        atMe.getBefore().setAfter(newFrob)
        atMe.setBefore(newFrob)
    if newF < me:
        while newF < me:
            me = (atMe.getBefore()).myName().lower()
            atMe = atMe.getBefore()
        newFrob.setAfter(atMe.getAfter())
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
        atMe.getAfter().setBefore(newFrob)
    else:
        newFrob.setAfter(atMe.getAfter())
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
        atMe.getAfter().setBefore(NewFrob)

a = Frob('a')
b = Frob('b')
d = Frob('d')
g = Frob('g')

a.setAfter(b)
b.setBefore(a)
b.setAfter(d)
d.setAfter(g)
d.setBefore(b)
g.setBefore(d)
