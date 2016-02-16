
#
#HW07
#
#Austin Chen
#
#This module contains problems 1-5 for Homework #7.
#

import math
import time

#
#This function will output the equation of a circle given the coordinate points
#of the diameter.
#   input: none
#

def circle():
    #These print and input statements gather the two points of information used for the circle.
    #Input is on a new line because I like having the cursor go to the next line for input.
    print("What is the x coordinate of your first point?")
    x1 = eval(input(""))
    print("What is the y coordinate of your first point?")
    y1 = eval(input(""))
    print("What is the x coordinate of your second point?")
    x2 = eval(input(""))
    print("What is the y coordinate of your second point?")
    y2 = eval(input(""))

    #These are the midpoints given the user's coordinate inputs
    midpointx = (x1 + x2)/2
    midpointy = (y1 + y2)/2

    #This is the distance formula using the user's coordinate inputs
    radius = ((((x2-x1)**2)+((y2-y1)**2))**.5)
    radius = round(radius, 2)
    print("The equation given these endpoints of the diameter is", "(x-",midpointx,")^2 + (y-",midpointy,")^2 =",radius)

#
#This function will solve an SAS triangle in terms of missing sides, angles, and total area.
#   input: none
#

def SAS():
    #User input for triangle information
    print("What is your SAS triangle?")
    time.sleep(.1)
    print("List your inputs in order of Side, Angle, Side. Format: [a,x,b] a = side, x = angle, b = side. ")
    a,x,b = eval(input(""))

    #Calculating cos(x) of the input degree. Not as efficient, but calculating seperately helps me organize
    x = math.radians(x)
    cosx = math.cos(x)

    #Law of Cosines
    missingSide1 = round((((a**2) + (b**2) - (2*a*b*cosx))**.5),2)

    #Law of Sines to calculate angles
    missingAngle1 = ((math.sin(x)) * (a))/missingSide1
    missingAngle1 = math.asin(missingAngle1)
    missingAngle1 = round(math.degrees(missingAngle1),2)

    #Finding the last angle through subtraction. Triangles have 180 degrees.
    missingAngle2 = 180 - missingAngle1 - originalX

    #Heron's Formula

    #Semiperimeter
    sP = 0.5*(a+b+missingSide1)
    #Heron's formula translation to code
    hFormula = ((sP)*(sP-a)*(sP-b)*(sP-missingSide1))**.5
    hFormula = round(hFormula,2)

    #Summation of information
    print("The 3rd side's length is:", missingSide1)
    print("The 1st missing angle is:", missingAngle1)
    print("The 2nd missing angle is:", round(missingAngle2,2))
    print("The area of the whole triangle is:",hFormula)

    #I realize I made things look really complicated by not using abc for sides and ABC for angles. Sorry 'bout that.


#
#This function will add values in the odd slots of a list and a seperate sum of the even slots of a list.
#   input: none
#

def everyOther():
    #User input for list to be analyzed
    print("Input a list of values. Format: [x,y,...,z]")
    x = eval(input(""))

    
    y = 1
    z = 2

    #Output assignment before ForLoop reassignment
    totalOdd = 0
    totalEven = 0

    #ForLoop for calculating the sum of odds
    for o in x:
        #If y is odd, y % 2 will be 1. 1 * o will provide the integer value of the list.
        o = (y % 2) * o
        #Because y represents the place in the list, y will rise by 1 each time.
        y = y + 1
        #totalOdd starts at 0 and adds what (y%2)*o equaled each time. Because y starts at 1, an odd number, it will add all odd values to the totalOdd.
        totalOdd = totalOdd + o

    #ForLoop for calculating the sum of evens
    for e in x:
        #This is the exact same as the ForLoop above except for the value z starts at. It must be offset by 1 from the original value to account for evens. Both even and odd numbers are spaced apart in the same manner. Z must start at 2 or any other even number.
        e = (z % 2) * e
        z = z + 1
        totalEven = totalEven + e

    #Print and summary of information
    print("The sum of the odd positioned numbers in that list is",totalOdd,".")
    print("The sum of the even positioned numbers in that list is",totalEven,".")

#
#This function will prompt the user for a number and will then convert it to binary.
#   input: none
#

def toBinary():
    #Initial input sequence
    print("Enter an integer to be converted to binary.")
    initialInt = eval(input(""))
    powerModifier = 0
    outputBin = 0
    #The range of values will be log2^the integer to 0. This is how many digits the binary will have.
    for i in range(int(math.log2(initialInt)), -1, -1):        
        #The loop will take the initialInt and mod by 2 to get either 0 or 1.
        outputBin = outputBin + (initialInt % 2)*(10**powerModifier)
        #As the loop progresses, the initialInt will be divided by 2.
        initialInt = int(initialInt/2)
        powerModifier = powerModifier + 1
    print(outputBin)
    #Credit goes to Kwate Quartey, he helped me in pseudocode in how to flip my reversed binary.

#
#This function will prompt the user for binary and will then convert it to an integer.
#   input: none
#

def fromBinary():
    #Input
    print("Enter binary to be converted to an integer.")
    binary = input("")

    #Variable assignment for the length of the binary input
    binLength = len(binary)
    #outputInt must be assigned to 0 before the ForLoop starts.
    outputInt = 0

    #Sequentially going through each value
    for i in binary:
        #As it loops each time, the binary list's length will need to decrease to move to the next power on the string of numbers.
        binLength = binLength-1
        #x is the power value to multiply each binary value by.
        x = 2**binLength
        #outputInt will collect all of the values and sum it together.
        outputInt = outputInt + (x*int(i))
    print(outputInt)


#
#This function prints the numbers 1-20 by using various combinations of four fours.
#   input:none
#

def magic4s():
    #0
    print(int((4-4)+(4-4)))
    
    #1
    print(int(44/44))
    
    #2
    print(int((4*4)/(4+4)))

    #3
    print(int((4+4+4)/4))

    #4
    print(int(((4-4)**4) + 4))

    #5
    print(int((math.sqrt(4)) + (math.sqrt(4)) + (4/4)))

    #6
    print(int(((4+4)/4) + 4))

    #7
    print(int((4+4)-(4/4)))

    #8
    print(int((4+4)+(4-4)))

    #9
    print(int(((math.factorial(4)-4)/4)+4))

    #10
    print(int((44-4)/4))

    #11
    print(int((44/(math.sqrt(4)+math.sqrt(4)))))

    #12
    print(int((44+4)/4))

    #13
    print(int((44/4)+math.sqrt(4)))

    #14
    print(int((4+4+4+math.sqrt(4))))

    #15
    print(int((44/4)+4))

    #16
    print(int(4+4+4+4))

    #17
    print(int((4*4)+(4/4)))

    #18
    print(int((4*4)+(4/math.sqrt(4))))

    #19
    print(int(math.factorial(4)-4-(4/4)))

    #20
    print(int(math.factorial(4)-4+4-4))
    
