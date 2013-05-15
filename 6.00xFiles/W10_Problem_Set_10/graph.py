# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedEdge(Edge):
    def __init__(self, src, dest, total, outd):
        Edge.__init__(self, src, dest)
        if outd > total:
            raise ValueError('Total distance smaller than outdoor distance')
        self.total = total
        self.outd = outd
    def getTotalDistance(self):
        return self.total
    def getOutdoorDistance(self):
        return self.outd
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.total, self.outd)


class WeightedDigraph(Digraph):
    def addNode(self, node):
        if node not in list(self.nodes):
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, wEdge):
        src = wEdge.getSource()
        dest = wEdge.getDestination()
        total = float(wEdge.getTotalDistance())
        outd = float(wEdge.getOutdoorDistance())
        if not(src in list(self.nodes) and dest in list(self.nodes)):
            raise ValueError('Node not in graph')
        idx = list(self.edges).index(src)
        nod = list(self.edges)[idx]
        self.edges[nod].append([dest, (total, outd)])
    def childrenOf(self, node):
        idx = list(self.edges).index(node)
        nod = list(self.edges)[idx]
        return [child[0] for child in self.edges[nod]]
    def hasNode(self, node):
        return node in list(self.nodes)
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} {3}\n'.format(res, k, d[0], d[1])
        return res[:-1]



def DFS(graph, start, end, path = []):
    #Assumes graph is a Digraph
    #Assumes start and end are nodes in graph
    path = path + [start]
    print 'Current DFS path:', path
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph, node, end, path)
            if newPath != None:
                return newPath
    return None

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', path
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSShortest(graph, node, end, path)
                if newPath != None:
                    shortest = newPath
    return shortest


na = Node('a')
nb = Node('b')
nc = Node('c')
nd = Node('d')
ne = Node('e')
nf = Node('f')
g = WeightedDigraph()
g.addNode(na)
g.addNode(nb)
g.addNode(nc)
g.addNode(nd)
g.addNode(ne)
g.addNode(nf)
e1 = WeightedEdge(na,nb,15,10)
e2 = WeightedEdge(na,nc,14,6)
e3 = WeightedEdge(nb,nc,3,1)
e4 = WeightedEdge(nb,ne,7,4)
e5 = WeightedEdge(ne,nf,23,20)
e6 = WeightedEdge(nf,nd,8,5)
e7 = WeightedEdge(nd,ne,11,10)
e8 = WeightedEdge(ne,nc,10,5)
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
g.addEdge(e4)
g.addEdge(e5)
g.addEdge(e6)
g.addEdge(e7)
g.addEdge(e8)

##g = WeightedDigraph()
##
##for src in 'abcde':
##    for des in 'zxy':
##        srcNode = Node(src)
##        desNode = Node(des)
##        g.addNode(srcNode)
##        g.addNode(desNode)
##        edge = WeightedEdge(srcNode,desNode,15,10)
##        g.addEdge(edge)
