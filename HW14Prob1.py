from graphics import *

class GraphicsGroup:
    
    def __init__(self, anchor):
        """ Initializes a class that stores information in a list such as anchorpoint and graphics object """
        self.anchor = [anchor]

    def getAnchor(self):
        """ Returns the anchorpoint stored in the GraphicsGroup object/list """
        return self.anchor[0].clone()
    
    def addObject(self, graphicsObject):
        """ Adds graphical object to the GraphicsGroup list """
        self.anchor.append(graphicsObject)

    def move(self,dx,dy):
        """ Moves the graphical objects and anchor points by dx and dy. """
        self.anchor[0].move(dx,dy)

    def draw(self,win):
        """ Draws all objects in GraphicsGroup list to win """
        for i in range(1,len(self.anchor)):
            self.anchor[i].draw(win)

    def undraw(self,win):
        """ Undraws all objects within GraphicsGroup list """
        for i in self.anchor:
            i.undraw()

    def display(self):
        """ Returns list """
        return self.anchor

#
# This function allows the user to choose between emoticons to draw in the window
#   input: none
#

def main():
    win = GraphWin("Emoticons", 600,600)

    # Priming read for while loop
    noError = False

    # I used a while loop for error rejection.
    while noError == False:

        # Entry box
        emoteIn = Entry(Point(300,330),1)
        emoteIn.draw(win)

        # Instruction text
        instruct1 = Text(Point(300,265), "What emoticon would you like to draw?")
        instruct1.draw(win)

        instruct2 = Text(Point(300,300), "1) Smiley Face  2) Stern Face  3) Sad Face")
        instruct2.draw(win)

        instruct3 = Text(Point(300,360), "Enter a number then click to confirm. Then click the screen to draw.")
        instruct3.draw(win)

        # Pause for user click to see what the user entered in the entry box
        win.getMouse()

        # Stores text in entry box to currentIn
        currentIn = emoteIn.getText()
        
        # Breaks while loop if valid input is met
        if (currentIn == str(1)) or (currentIn == str(2)) or (currentIn == str(3)):
            noError = True
        # Loops back if invalid input
        else:
            emoteIn.undraw()
            instruct1.undraw()
            instruct2.undraw()
            instruct3.undraw()
            
    # Graphical undraws for progression
    emoteIn.undraw()
    instruct1.undraw()
    instruct2.undraw()
    instruct3.undraw()

    # More instruction prompt
    midPrompt = Text(Point(300,580), "Click again to place emoticon")
    midPrompt.draw(win)

    # User clicks and coordinates are stored in x and y
    mouseClick = win.getMouse()
    x = mouseClick.getX()
    y = mouseClick.getY()

    midPrompt.undraw()

    # Uses GraphicsGroup class to store click as the anchorpoint
    graphOb = GraphicsGroup(Point(x,y))

    # Defining the basic structure of the emoticon
    faceOutline = Circle(Point(x,y),30)
    faceOutline.setFill('yellow')
    
    leftEye = Circle(Point(x-10,y-10),5)
    leftEye.setFill('black')
    
    rightEye = Circle(Point(x+10,y-10),5)
    rightEye.setFill('black')

    # Defining dictionary for emoticon attributes
    faceDict = {'faceOutline':faceOutline,'leftEye':leftEye,'rightEye':rightEye}

    # Add face attributes to GraphicsGroup list
    graphOb.addObject(faceOutline)
    graphOb.addObject(leftEye)
    graphOb.addObject(rightEye)
    
    # Depending on what emoticon the user wants, the program will draw a different mouth
    if currentIn == str(1):
        # Drawing a smile
        leftSmile = Line(Point(x-13,y+9),Point(x,y+14))
        graphOb.addObject(leftSmile)
        rightSmile = Line(Point(x+13,y+9),Point(x,y+14))
        # Adds this smile to GraphicsGroup
        graphOb.addObject(rightSmile)
        # Draws everything
        graphOb.draw(win)
        
        # Adding left and right smile to dictionary
        faceDict['leftSmile'] = leftSmile
        faceDict['rightSmile'] = rightSmile

    elif currentIn == str(2):
        # Drawing flat smile
        sternSmile = Line(Point(x-14,y+12),Point(x+14,y+12))
        # Adds smile to GraphicsGroup
        graphOb.addObject(sternSmile)
        # Draws everything in GraphicsGroup
        graphOb.draw(win)
        
        # Adding stern smile to dictionary
        faceDict['sternSmile'] = sternSmile

    elif currentIn == str(3):
        # Drawing a frown, the opposite of the smile
        leftFrown = Line(Point(x-13,y+14),Point(x,y+9))
        graphOb.addObject(leftFrown)
        rightFrown = Line(Point(x+13,y+14),Point(x,y+9))
        graphOb.addObject(rightFrown)
        graphOb.draw(win)

        faceDict['leftFrown'] = leftFrown
        faceDict['rightFrown'] = rightFrown

    end = Text(Point(300,580), "Restart to draw another emoticon")
    end.draw(win)

    win.getMouse()
    win.close()
        
main()
    
