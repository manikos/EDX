# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.

    i.e 3x3 room is indexed as follows:
         _____ _____ _____
        |     |     |     |
        |(0,2)|(1,2)|(2,2)|
        |_____|_____|_____|
        |     |     |     |
        |(0,1)|(1,1)|(2,1)|
        |_____|_____|_____|
        |     |     |     |
        |(0,0)|(1,0)|(2,0)|
        |_____|_____|_____|
     """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        assert width>0 and height>0, "Negative diamensions?"
        self.width = width
        self.height = height
        self.tiles = {}
        for w in range(width):
            for h in range(height):
                self.tiles[(w,h)] = False
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tiles[( int(pos.getX()), int(pos.getY()) )] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m, n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleanTiles=0
        for cleaned in self.tiles.values():
            if cleaned: cleanTiles+=1
        return cleanTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.random()*self.width, random.random()*self.height)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return pos.getX() < self.width and pos.getX() >=0 and pos.getY() < self.height and pos.getY() >=0


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room #self.room is a RectangularRoom instance
        self.direction = random.randrange(0, 360)
        self.position = room.getRandomPosition() #self.position is a Position instance
        room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #Orizw neo instance to opoio tha ypologizei tin mellontiki kinisi tou robot
        nextPosition = self.position.getNewPosition( self.getRobotDirection(), self.speed )

        #an i epomeni kinisi tou robot einai ektos oriwn, tote ypologizei nea dieythinsi
        if not self.room.isPositionInRoom( nextPosition ):
            self.setRobotDirection( random.randrange(0, 360) )
        #an i epomeni kinisi tou robot einai entos oriwn, metakinw to robot sti nea thesi
        else:
            self.setRobotPosition( self.position.getNewPosition( self.getRobotDirection(), self.speed ) )
            self.room.cleanTileAtPosition( self.getRobotPosition() )
            

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    assert num_robots>0 and speed>0 and width>0 and height>0 and num_trials>0 \
           and min_coverage<=1.0 and min_coverage>=0, "Wrong value of argument"
    counter = [0 for i in range(num_trials) ]

    for num in range(num_trials):
        anim = ps7_visualize.RobotVisualization(num_robots, width, height,) #VISUALIZE 1
        room = RectangularRoom(width, height) #instantiation of RectangularRoom
        robots = [ robot_type( room, speed ) for i in range(num_robots) ]
        
        while room.getNumCleanedTiles() / float(room.getNumTiles()) < min_coverage :
            for r in range(num_robots):
                anim.update(room, robots) #VISUALIZE 2
                robots[r].updatePositionAndClean()
            counter[num]+=1
            if room.getNumCleanedTiles() / float(room.getNumTiles()) == min_coverage :
                break
    anim.done() #VISUALIZE 3

    total_moves = 0
    for moves in counter:
        total_moves += moves

    mean_number = total_moves/float(num_trials)

    return mean_number


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #Orizw neo instance to opoio tha ypologizei tin mellontiki kinisi tou robot
        nextPosition = self.position.getNewPosition( self.getRobotDirection(), self.speed )

        #an i epomeni kinisi tou robot einai ektos oriwn, tote ypologizei nea dieythinsi
        if self.room.isPositionInRoom( nextPosition ):
            self.setRobotPosition( self.position.getNewPosition( self.getRobotDirection(), self.speed ) )
            self.room.cleanTileAtPosition( self.getRobotPosition() )
            self.setRobotDirection( random.randrange(0, 360) )
        else:
            self.setRobotDirection( random.randrange(0, 360) )

# === Problem Nik     
class NickRobot(Robot):
    """
    A NickRobot is a Robot with an improved-smarter standard movement strategy.

    At each time-step, a NickRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly (but not towards the wall again).
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #Orizw neo instance to opoio tha ypologizei tin mellontiki kinisi tou robot
        nextPosition = self.position.getNewPosition( self.getRobotDirection(), self.speed )

        #An i epomeni kinisi tou robot einai ENTOS Oriwn proxwra sto idio direction
        if self.room.isPositionInRoom( nextPosition ):
            self.setRobotPosition( self.position.getNewPosition( self.getRobotDirection(), self.speed ) )
            self.room.cleanTileAtPosition( self.getRobotPosition() )
        #An einai EKTOS Oriwn ypologizei nea dieythinsi i opoia tha deixnei entos
        else:
            #upper left corner
            if int(self.position.getX())==0 and int(self.position.getY())==self.room.height-1:
                self.setRobotDirection( random.randrange(90, 181) )
            #upper right corner
            elif int(self.position.getX())==self.room.width-1 and int(self.position.getY())==self.room.height-1:
                self.setRobotDirection( random.randrange(180, 271) )
            #bottom right corner
            elif int(self.position.getX())==self.room.width-1 and int(self.position.getY())==0:
                self.setRobotDirection( random.randrange(270, 360) )
            #bottom left corner
            elif int(self.position.getX())==0 and int(self.position.getY())==0:
                self.setRobotDirection( random.randrange(0, 91) )
            #upper wall not including edges
            elif int(self.position.getX()) in range(1,self.room.width-1) and int(self.position.getY())==self.room.height-1:
                self.setRobotDirection( random.randrange(90, 271) )
            #right wall not including edges
            elif int(self.position.getX())==self.room.width-1 and int(self.position.getY()) in range(1,self.room.height-1):
                self.setRobotDirection( random.randrange(180, 360) )
            #bottom wall not including edges
            elif int(self.position.getX()) in range(1,self.room.width-1) and int(self.position.getY())==0:
                self.setRobotDirection( (random.randrange(180, 360)+90)%359 )
            #left wall not including edges
            else:
                self.setRobotDirection( random.randrange(0, 181) )

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

def showPlot3(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    times3 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, NickRobot))
        times3.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.plot(num_robot_range, times3)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'NickRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room ', 'Number of Robots ', 'Time-steps' )
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#showPlot2('Time It Takes A Robot To Clean 80% Of Variously Shaped Rooms ', 'Aspect Ratio', 'Time-steps' )
#
