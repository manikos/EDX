class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        # mom_node is Member instance
        mom_node = self.names_to_nodes[mother]
        # add each child
        for c in list_of_children: 
            # create Member node for a child
            c_member = Member(c)
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member
            # set child's parent
            c_member.add_parent(mom_node)
            # set the parent's child
            mom_node.add_child(c_member)
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)


    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed)

        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common
        ancestor as described in 5-2.

        degree removed is the distance to the common ancestor

        Keyword arguments:
        a -- string that is the name of a
        b -- string that is the name of b
        """
        node_a = self.names_to_nodes[a]
        node_b = self.names_to_nodes[b]
        # if a and b are the same node or if one is the direct descendent of the other
        if node_a == node_b:
            return (-1, 0)
        elif (node_a.is_parent(node_b) or node_b.is_parent(node_a)):
            return (-1, 1)
        
        
        def find_depth(one, depth = -2):
            if one == None:
                return depth
            else:
                return find_depth(one.get_parent(), depth+1)
        
        depth_node_a = find_depth(node_a)
##        print 'final depth for', str(node_a), '=', depth_node_a

        depth_node_b = find_depth(node_b)
##        print 'final depth for', str(node_b), '=', depth_node_b

        counter_a, counter_b = False, False
        if depth_node_b > depth_node_a:
            counter_b == 0
            while node_b != node_a:
                counter_b += 1
                node_b = node_b.get_parent()
                if node_b is None:
                    counter_b = False
                    break
            if counter_b != 0:
                while node_a != self.root:
                    counter_b += 1
                    node_a = node_a.get_parent()

        if depth_node_a > depth_node_b:
            counter_a == 0
            while node_a != node_b:
                counter_a += 1
                node_a = node_a.get_parent()
                if node_a is None:
                    counter_a = False
                    break
            if counter_a != 0:
                while node_b != self.root:
                    counter_a += 1
                    node_b = node_b.get_parent()

        if counter_a != False:
            return ( -1, counter_a )
        elif counter_b != False:
            return ( -1, counter_b )
        else:
            return (min(depth_node_a, depth_node_b), abs(depth_node_a - depth_node_b)) 



f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("a", "h")
print "'a' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("h", "b")
print "'h' is a", words[t], "cousin", r, "removed from 'b'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("b", "l")
print "'b' is a", words[t], "cousin", r, "removed from 'l'"

t, r = f.cousin("b", "k")
print "'b' is a", words[t], "cousin", r, "removed from 'k'"

t, r = f.cousin("e", "k")
print "'e' is a", words[t], "cousin", r, "removed from 'k'"
