# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph.

# This particular graph will be a Weighted Graph. This means that,
# will consist of Nodes, Edges and 2 different kind of weights.
# Nodes will be represented as strings - Building Numbers (buildID)
# Edges will be represented as virual path connecting 2 buildings.
# Weights will be represented as numbers showing the total distance
# and the distance which is outdoor.
# e.g The file mit_map.txt has data in it in the form:
#                10 32 200 40
# which means:
# The map contains an edge from building 10 (source) to building
# 32 (dest) that is 200 meters long, where 40 of 200 meters are outside.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: mapFilename : name of the map file (mit_map.txt)

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns: a directed graph representing the map
    """
    print "Loading map from file..."
    # Store data from file to 4 different lists
    inFile=open(mapFilename, 'r', 0)
    src, dest, total, outd = [], [], [], []
    for line in inFile:
        s = line.strip('\n')
        fields = s.split(' ')
        src.append(fields[0])
        dest.append(fields[1])
        total.append(int(fields[2]))
        outd.append(int(fields[3]))

    #Building the Weighted-Digraph.
    #1st: Build a Weighted-Digraph
    #2nd: Build the Nodes (Sources & Destinations)
    #3rd: Add Nodes to Weighted-Digraph
    #4th: Build the Edges
    #5th: Add Edges to Weighted-Digraph
    g = WeightedDigraph()
    for i in range(len(src)):
        sr, ds = Node(src[i]), Node(dest[i])
        g.addNode(sr)
        g.addNode(ds)
        edge = WeightedEdge(sr, ds, total[i], outd[i])
        g.addEdge(edge)
    print "Map successfully loaded."
    return g

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are:
#
# The goal is to find the shortest route (or path) that leads from a start
# Node to an end one, under the condition that the total distance travelled
# will not exceed either the maxTotalDist and the maxDistOutdoors.
#
# This means that ALL the possible routes will be examined. The winner will
# be the one that fullfils the above conditions.
#

def DFS(graph, start, end, path = []):
    """
    Depth-First Search algorithm

    parameters: graph: instance of WeightedGraph class
                start, end: instances of Node class
    Assumes that start+end Nodes are in the graph

    yields: lists (representing all possible paths from start to end)
    """
    path = path + [start]
    #print 'Current DFS path:', path
    if start == end:
        yield path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph, node, end, path)
            for nPath in newPath:
                yield nPath


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    gen_paths = DFS(digraph, Node(start), Node(end))
    valid_paths = []
    total_dists= []
    
    for path in gen_paths: #path form: [a,b,c]
        totald, outd = 0, 0
        for i in range(len(path)-1): #scan each node except last one
            indx = list(digraph.edges).index(path[i])
            nod = list(digraph.edges)[indx]
            nodes = digraph.edges[nod]
            for posib_node in nodes: #posib_node form: [b, (3,2)]
                if posib_node[0] == path[i+1]:
                    totald += posib_node[1][0]
                    outd += posib_node[1][1]
        if totald <= maxTotalDist and outd <= maxDistOutdoors:
            valid_paths.append(path)
            total_dists.append(totald)

    if len(valid_paths) == 0:
        raise ValueError
    else:
        str_valid_path = valid_paths[ total_dists.index(min(total_dists)) ]
        return [ str(p) for p in str_valid_path ]


#
#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
#

def DFSShortest(graph, start, end, maxTotalDist, maxDistOutdoors, path = [],\
                distance = None, dist_out = None):
    """
    Optimized Depth-First Search algorithm

    parameters: graph: instance of WeightedGraph class
                start, end: instances of Node class
    Assumes that start+end Nodes are in the graph

    yields: list (1st element= total distance, 2nd element=path)
    """
    path = path + [start]
    #initialization of the distance & dist_out
    if (distance is None) or (dist_out is None):
        distance, dist_out = [], []
    #if start==end 
    if start == end:
        yield sum(distance)
        yield path
    for node in graph.childrenOf(start):
        #avoid cycles AND do not go further if node is the goal
        if (node not in path) and (start != end):
            #search and find the appropriate distances (total & outdoor)
            for n in graph.edges[ list(graph.nodes)[list(graph.nodes).index(Node(start))] ]:
                if n[0] == node:
                    distance.append(n[1][0])
                    dist_out.append(n[1][1])
            #if constraints are met, compute next path
            if sum(distance) <= maxTotalDist and sum(dist_out) <= maxDistOutdoors:
                newPath = DFSShortest(graph, node, end, maxTotalDist, maxDistOutdoors, path, distance, dist_out)
            #go one level up (for the computation of the next path)
                distance = distance[:-1]
                dist_out = dist_out[:-1]
                for nPath in newPath:
                    yield nPath
            #if constraints are not met, go one level up for the next path
            else:
                distance = distance[:-1]
                dist_out = dist_out[:-1]
                

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
    not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    gen_paths = DFSShortest(digraph, Node(start), Node(end), maxTotalDist, maxDistOutdoors)
    data, total_dists, valid_paths = [], [], []
    i = 0
    #fill the lists with the appropriate data (distance & path)
    #data is in form: [ 34.0, [a,b,c], 54.0, [a,c] ]
    for path in gen_paths:
        data.append(path)
    while i < len(data):
        if i%2 == 0:
            total_dists.append(data[i]) #list of floats
        else:
            valid_paths.append(data[i]) #list of lists
        i += 1
    #return the path bind with the shortest distance else raise ValueError
    if len(valid_paths) == 0:
        raise ValueError
    else:
        str_valid_path = valid_paths[ total_dists.index(min(total_dists)) ]
        return [ str(p) for p in str_valid_path ]
        

mitMap = load_map("mit_map.txt")

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges


#     LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

