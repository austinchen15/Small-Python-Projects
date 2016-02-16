#
# HW10Prob3
#
# Austin Chen
#
# This module contains problem #3 for Homework #10
#

import math
import graphics
from graphics import *

#
# This function will return the distance between points p1 and p2.
#   input: p1, p2
#   output: distance between p1,p2
#

def distance(p1,p2):
    #Distance formula
    dist =  math.sqrt(((p2.getX()-p1.getX())**2)+((p2.getY()-p1.getY())**2))
    return dist

#
# This function will graph a circle with facial components
#   input: p, r, win
#   output: Graphics
#

def face(p,r,win):
    # Graphing circle with center p and radius r. Both are inputs by user.
    face = Circle(p,r)
    face.setFill('yellow')
    face.draw(win)

    # Face component 1
    # eye2's r/4 and r/9 are to correctly scale and position.
    eye1 = Circle(Point(p.getX()-r/4,p.getY()-r/4), r/9)
    eye1.setFill('black')
    eye1.draw(win)

    # Face component 2
    # eye2's r/4 and r/9 are to correctly scale and position.
    eye2 = Circle(Point(p.getX()+r/4,p.getY()-r/4), r/9)
    eye2.setFill('black')
    eye2.draw(win)

    # Face component 3
    # Uses triangle as smile, r/n is similar scaling and positioning as before.
    smile = Polygon(Point(p.getX()-r/2.5,p.getY()+r/5), Point(p.getX()+r/2.5,p.getY()+r/5), Point(p.getX(),p.getY()+r/2))
    smile.setFill('black')
    smile.draw(win)
    

#
# This is the main function. Will prompt user for image and number of faces.
# Within the graphics window, the user's clicks will register two points.
# These two points (p1,p2) will be used by the distance function and face function.
#   input: none
#

def main():

    # Gather user input for file and number of faces
    userFile = input("Photo to import (gif or ppm): ")
    faces = eval(input("Number of faces to cover: "))
    
    print("For each face, click the center and a point on the edge.")

    # Constructing the window based on the image size
    file = Image(Point(0,0), userFile)
    x = file.getWidth()
    y = file.getHeight()
    # Uses x and y as window size
    win = GraphWin("Cartoon Faces",x,y)
    # Graphics Image method. x/2 and y/2 will always center the image.
    Image(Point(x/2,y/2), userFile).draw(win)

    # Will loop as many times the user specifies
    for i in range(faces):
        # User input for mouse clicks
        p1 = win.getMouse()
        p2 = win.getMouse()
        # Uses the distance function with the previous p1 and p2 as input
        # Saves in r, to be used as function face input
        r = distance(p1,p2)
        # Uses the face function to graph
        face(p1,r,win)

    # After the user is done creating faces, will start exit prompt
    # Rectangle background
    exitRect = Rectangle(Point(x/2.5,y/2.5),Point(x-(x/2.5),y-(y/2.5)))
    exitRect.setFill('white')
    exitRect.draw(win)

    # Exit dialogue
    exitDial = Text(Point(x/2,y/2),"Click twice to exit")
    exitDial.draw(win)
    
    # Mouse clicks to close
    win.getMouse()
    exitRect.undraw()
    exitDial.undraw()
    win.getMouse()
    win.close()
    
main()
    
    
