def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beggining of the linked list
    """
    if start.getBefore() is None:
        return start
    else:
        return findFront(start.getBefore())

