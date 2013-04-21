class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    def __repr__(self):
        s='Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'
        return s
