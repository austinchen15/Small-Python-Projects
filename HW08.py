#
# HW08
#
# Austin Chen
#
# Homework #8 Problems 1-3
#

import math
import random
from graphics import *

#
#Problem 1
#Cartoon Character, this function will recreate the image of Stewie Griffin using 15+ shapes.
#Picture of character: http://tvcinemaemusica.files.wordpress.com/2009/10/7510stewie.jpg
#   input: none
#

def character():
    window = GraphWin("Cartoon Character", 600, 600)
    window.setCoords(-100,-100,100,100)

    cream = color_rgb(245,223,188)
    redClothes = color_rgb(230,3,0)
    yellowClothes = color_rgb(250,250,0)
    blueShoes = color_rgb(188,233,245)
    backgroundBlue = color_rgb(0,119,217)

    window.setBackground(backgroundBlue)

    #All the seperate components are in an order that will overlap the shapes correctly.

    #1
    #Left Ear
    leftEar = Circle(Point(-60,36),5)
    leftEar.setFill(cream)
    leftEar.draw(window)
          
    #2
    #Right Ear
    rightEar = leftEar.clone()
    rightEar.move(120,0)
    rightEar.draw(window)
          
    #3
    #Left Ear outline to give inner contour
    leftInnerEar = Circle(Point(-60,35.3),2.6)
    leftInnerEar.draw(window)

    #4
    #Right Ear outline to give inner contour
    rightInnerEar = leftInnerEar.clone()
    rightInnerEar.move(120,0)
    rightInnerEar.draw(window)
          
    #5
    #Red Clothes
    chest1 = Rectangle(Point(-25,14),Point(25,-14))
    chest1.setFill(yellowClothes)
    chest1.draw(window)
          
    #6
    #Left red overall strap
    leftStrap = Rectangle(Point(-25,15),Point(-10,-40))
    leftStrap.setFill(redClothes)
    leftStrap.draw(window)
          
    #7
    #Right red overall strap
    rightStrap = leftStrap.clone()
    rightStrap.move(35,0)
    rightStrap.draw(window)
          
    #8
    #Red pants legs
    legs = Rectangle(Point(-25,-40),Point(25,-75))
    legs.setFill(redClothes)
    legs.draw(window)
          
    #9
    #This red outlined rectangle masks the outlines from the previous shapes.
    chest2 = Rectangle(Point(-24,-14),Point(24,-40))
    chest2.setFill(redClothes)
    chest2.setOutline(redClothes)
    chest2.draw(window)
          
    #10
    #This shape is to create a black border line between the red and yellow.
    chestOutline = Line(Point(-10,-14),Point(10,-14))
    chestOutline.draw(window)
          
    #11
    #Left button
    leftButton = Circle(Point(-17.5,-10),4.3)
    leftButton.setFill(yellowClothes)
    leftButton.draw(window)
          
    #12
    #Right button
    rightButton = leftButton.clone()
    rightButton.move(35,0)
    rightButton.draw(window)
          
    #13
    #This is to create a division to shape the legs
    legDivide1 = Line(Point(0,-40),Point(0,-75))
    legDivide1.draw(window)
          
    #14
    #This thickens the line, to provide a larger border to differentiate between legs
    legDivide2 = Line(Point(-.1,-40),Point(-.1,-75))
    legDivide2.draw(window)
          
    #15
    #Further leg division
    legDivide3 = Line(Point(-.1,-40),Point(-3,-38))
    legDivide3.draw(window)
          
    #16
    #Further leg division
    legDivide4 = Line(Point(0,-40),Point(3,-38))
    legDivide4.draw(window)
          
    #17
    #Left shoe
    leftShoe = Oval(Point(-28,-68),Point(0,-80))
    leftShoe.setFill(blueShoes)
    leftShoe.draw(window)
          
    #18
    #Right shoe
    rightShoe = leftShoe.clone()
    rightShoe.move(25.3,0)
    rightShoe.draw(window)
          
    #19
    #Left hand
    leftHand = Oval(Point(-36,-30),Point(-25,-35.7))
    leftHand.setFill(cream)
    leftHand.draw(window)
          
    #20
    #Right hand
    rightHand = leftHand.clone()
    rightHand.move(60.5,0)
    rightHand.draw(window)
          
    #21
    #Left arm
    leftArm = Rectangle(Point(-35.8,8),Point(-25,-33))
    leftArm.setFill(yellowClothes)
    leftArm.draw(window)
          
    #22
    #Right arm
    rightArm = leftArm.clone()
    rightArm.move(60.5,0)
    rightArm.draw(window)
          
    #23
    #Shape of the face
    face = Oval(Point(-60,72), Point(60,0))
    face.draw(window)
    face.setFill(cream)
          
    #24
    #Left eye
    leftEye = Circle(Point(-23,35), 13)
    leftEye.setFill('white')
    leftEye.draw(window)
          
    #25
    #Right eye
    rightEye = leftEye.clone()
    rightEye.move(46,0)
    rightEye.setFill('white')
    rightEye.draw(window)
          
    #26
    #Left pupil, is contained within leftEye
    leftPupil = Circle(Point(-26,33.8),1.3)
    leftPupil.setFill('black')
    leftPupil.setOutline('black')
    leftPupil.draw(window)
          
    #27
    #Right pupil, is contained within rightEye
    rightPupil = leftPupil.clone()
    rightPupil.move(46,-.2)
    rightPupil.draw(window)
          
    #28
    #Left eyebrow
    leftEyebrow = Line(Point(-35,53),Point(-11,48.5))
    leftEyebrow.draw(window)
          
    #29
    #Right eyebrow
    rightEyebrow = Line(Point(35,53),Point(11,48.5))
    rightEyebrow.draw(window)
          
    #30
    #Top line of nose
    noseTop = Line(Point(1,30),Point(-3,25))
    noseTop.draw(window)
          
    #31
    #Bottom line of nose, is joined to top to create an angle that shapes the nose
    noseBottom = Line(Point(-3,25),Point(0.2,23))
    noseBottom.draw(window)
          
    #32
    #Mouth
    mouth1 = Line(Point(-4.5,15.3),Point(-7.5,12))
    mouth1.draw(window)
          
    #33
    #Mouth
    mouth2 = Line(Point(-7.5,12),Point(6.5,12))
    mouth2.draw(window)
          
    #34
    #Mouth
    mouth3 = Line(Point(-4.5,12),Point(-0.5,9))
    mouth3.draw(window)
          
    #35
    #Black line that helps create the resemblance of fingers
    leftFinger1 = Line(Point(-32.2,-34),Point(-32.2,-35.3))
    leftFinger1.draw(window)
          
    #36
    #Black line that helps create the resemblance of fingers
    leftFinger2 = leftFinger1.clone()
    leftFinger2.move(3.8,0)
    leftFinger2.draw(window)
          
    #37
    #Black line that helps create the resemblance of fingers
    rightFinger1 = leftFinger1.clone()
    rightFinger1.move(60.5,0)
    rightFinger1.draw(window)

    #38
    #Black line that helps create the resemblance of fingers
    rightFinger2 = leftFinger2.clone()
    rightFinger2.move(60.5,0)
    rightFinger2.draw(window)

    window.getMouse()
    window.close()    
    
character()        

#
#Problem 2: This function will plot the mathematical function with a specified xmin, xmax, and number of points.
#   input:none
#
def graph():
    #Set window size and initial coordinate system
    window = GraphWin("Graph",500,500)
    window.setCoords(-100,-100,100,100)

    #Prompt box and label for Min X input
    minXLabel = Text(Point(-85,90),"Min X:")
    minXLabel.draw(window)
    minX = Entry(Point(-68,90),5)
    minX.draw(window)

    #Prompt box and label for Max X input
    maxXLabel = Text(Point(-85,77.5),"Max X:")
    maxXLabel.draw(window)
    maxX = Entry(Point(-68,77.5),5)
    maxX.draw(window)

    #Prompt box and label for increment (N) input
    nLabel = Text(Point(-63.95,65),"Number of points to plot (N):")
    nLabel.draw(window)
    n = Entry(Point(-25,65),5)
    n.draw(window)

    #X and Y axis lines
    yAxis =Line(Point(0,96),Point(0,-96))
    yAxis.draw(window)
    xAxis = Line(Point(-96,0),Point(96,0))
    xAxis.draw(window)

    #Endlines on X and Y axis
    Line(Point(-96,3),Point(-96,-3)).draw(window)
    Line(Point(96,3),Point(96,-3)).draw(window)

    #Graphical additions to the end of the axes, these lines are inefficient because I was experimenting and needed to assign these lines
    yAxisEndlinePos = Line(Point(-3,96),Point(3,96))
    yAxisEndlinePos.draw(window)
    yAxisEndlineNeg = Line(Point(-3,-96),Point(3,-96))
    yAxisEndlineNeg.draw(window)

    #Instructions
    graphText = Text(Point(-50,-90),"Click anywhere on the screen to begin graphing")
    graphText.draw(window)

    #Program will be paused until mouse is clicked
    window.getMouse()

    #This will make the text disappear
    graphText.undraw()
    minX.undraw()
    maxX.undraw()
    minXLabel.undraw()
    maxXLabel.undraw()
    nLabel.undraw()
    n.undraw()

    #Assigning input to variables, need eval to transform into strings
    minXIn = eval(minX.getText())
    maxXIn = eval(maxX.getText())
    nIn = int(eval(n.getText()))

    #Visual graph scale on both axes
    Text(Point(-95,-6.3),minXIn).draw(window)
    Text(Point(95,-6.3),maxXIn).draw(window)
    Text(Point(-8,95.6),"5").draw(window)
    Text(Point(-8,-96),"-5").draw(window)


    #Readjust coordinate system to account for user's xMin and xMax
    window.setCoords((minXIn),-5,(maxXIn),5)

    #Initial point the drawing will start with. Will then move to ForLoop
    #Equation will output a y given the initial minX.
    y = 3*math.sin(minXIn/2)-math.cos((2*minXIn)+(math.pi/4))
    point1 = Point(minXIn,y)
    point1.draw(window)

    #This equation calcuates how far each point will be from the next.
    #To be used in ForLoop, rounded values
    step = round(abs((maxXIn-minXIn)/nIn),3)

    #Range: N, how many dots the user specified.
    for i in range(nIn):
        #After min
        minXIn = minXIn + step
        y = 3*math.sin(minXIn/2)-math.cos((2*minXIn)+(math.pi/4))
        point2 = Point(minXIn,y)
        point2.draw(window)
        pointConnect = Line(point1,point2)
        pointConnect.draw(window)
        #Similar to the Fibonacci reassigment I used on the test, this will shift each point over left to right
        point1 = point2

    
    
    window.getMouse()
    window.close() 

graph()


#
#Problem 3 - Bingo
#This function will draw a random BINGO card every time it is run.
#   input: none
#

def bingo():
    #Defining window size
    window = GraphWin("Bingo",750,750)
    window.setCoords(-120,-120,120,120)

    #Outline of bingo board
    outline = Rectangle(Point(-100,100),Point(100,-100))
    outline.draw(window)

    #Grid on bingo board
    Line(Point(-60,100),Point(-60,-100)).draw(window)
    Line(Point(-20,100),Point(-20,-100)).draw(window)
    Line(Point(20,100),Point(20,-100)).draw(window)
    Line(Point(60,100),Point(60,-100)).draw(window)
    Line(Point(-100,60),Point(100,60)).draw(window)
    Line(Point(-100,20),Point(100,20)).draw(window)
    Line(Point(-100,-20),Point(100,-20)).draw(window)
    Line(Point(-100,-60),Point(100,-60)).draw(window)

    #B label at top
    B = Text(Point(-80,110),"B")
    B.setSize(36)
    B.draw(window)

    #I label at top
    I = Text(Point(-40,110),"I")
    I.setSize(36)
    I.draw(window)

    #N label at top
    N = Text(Point(0,110),"N")
    N.setSize(36)
    N.draw(window)

    #G label at top
    G = Text(Point(40,110),"G")
    G.setSize(36)
    G.draw(window)

    #O label at top
    O = Text(Point(80,110),"O")
    O.setSize(36)
    O.draw(window)

    #Free label
    Free = Text(Point(0,5),"FREE")
    Free.setSize(24)
    Free.draw(window)

    #Space label
    Space = Text(Point(0,-5),"SPACE")
    Space.setSize(24)
    Space.draw(window)

    #Column B random number generator, range is 1-15 for each cell
    #yMod is the starting Y coordinate
    yMod = 80
    #Forloop will repeat it five times and move the text down a box each time
    for i in range(5):
        cellNumb = Text(Point(-80,yMod),random.randint(1,15))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        #As the ForLoop continues
        yMod = yMod - 40

    #Column I random number generator, range is 16-30 for each cell
    yMod = 80
    #Forloop will repeat it five times and move the text down a box each time
    for i in range(5):
        cellNumb = Text(Point(-40,yMod),random.randint(16,30))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        yMod = yMod - 40

    #Column N random number generator, range is 31-45 for each cell
    #In this case, the loop will only repeat twice so that it stops before the "Free Space"
    yMod = 80
    for i in range(2):
        cellNumb = Text(Point(0,yMod),random.randint(31,45))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        yMod = yMod - 40

    #Column N random number generator, range is 31-45 for each cell
    #Random number generator resumes for two more loops after skipping "Free Space"
    yMod = -40
    for i in range(2):
        cellNumb = Text(Point(0,yMod),random.randint(31,45))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        yMod = yMod - 40
    
    #Column G random number generator, range is 46-60 for each cell
    yMod = 80
    #Forloop will repeat it five times and move the text down a box each time
    for i in range(5):
        cellNumb = Text(Point(40,yMod),random.randint(46,60))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        yMod = yMod - 40
        
    #Column O random number generator, range is 61-75 for each cell
    yMod = 80
    #Forloop will repeat it five times and move the text down a box each time
    for i in range(5):
        cellNumb = Text(Point(80,yMod),random.randint(61,75))
        cellNumb.setSize(36)
        cellNumb.draw(window)
        yMod = yMod - 40        
    
    #User input for 5 dots

    #ForLoop for snapping dots to center
    for i in range(5):
        #P1 will store the coordinates of the mouse click
        p1 = window.getMouse()
        #X coordinate will first be divided by 40 because each cell's center is spaced 40 apart.
        #Dividing by 40 then the subsequent rounding will transform each value to an integer.
        #Then, multiply back by 40 to scale it up to the -100,-100,100,100 coordinate scale.
        x = round(p1.getX()/40)*40
        y = round(p1.getY()/40)*40
        userCircle = Circle(Point(x,y),15)
        userCircle.setFill('cyan4')
        userCircle.setOutline('purple3')
        userCircle.draw(window)

    for i in range(5):
        #Computer will choose random coordinates on my scale and return x and y
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        #Similar center snapping as before
        x = round(x/40)*40
        y = round(y/40)*40
        compCircle = Circle(Point(x,y),15)
        compCircle.setFill('purple4')
        compCircle.setOutline('cyan3')
        compCircle.draw(window)

    window.getMouse()
    window.close()

bingo()
