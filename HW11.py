#
# HW11
#
# Austin Chen
#
# This module contains homework problems for Homework #11
#

from math import sqrt
from graphics import *

#
# This function will determine a speeding fine in Winter Wonderland (if necessary)
#   input: none
#

def speedingTicket():
    try:
        # Gathering input from user
        limit = eval(input("Enter the speed limit: "))
        speed = eval(input("Enter the clocked speed: "))

        # How far over the speed limit you are
        speedOver = speed-limit
        # Calculating the fine
        fine = 50 + ((speedOver)*5)

        statement = ""

        # Conditions of the relationship between speed and limit
        if speed >= 0 and limit >=0:
            if speed <= limit:
                print("The given clocked speed is legal. ")
            elif speed > limit and speed <= (limit + 25):
                # Printing if the speed is within 25mph over limit
                statement = "Your speed is " + str(speedOver) + " MPH over the speed limit.\nThe fine will be $" + str(fine) + "."
                print(statement)
            elif speed > (limit + 25):
                # Fine will increase by 200 if speed is over 25mph beyond the speed limit.
                fine = fine + 200
                statement = "Your speed is " + str(speedOver) + " MPH over the speed limit.\nThe fine will be $" + str(fine) +"."
                print(statement)
        else:
            print("\nError: You can't have a negative speed.\n")
            speedingTicket()

    # Exceptions for this function
    except NameError:
        print("\nError: You did not enter a number.\n")
        speedingTicket()
    except SyntaxError:
        print("\nError: Your input format was wrong.\n")
        speedingTicket()
    except TypeError:
        print("\nYou did not enter a proper number.\n")
        speedingTicket()
    except:
        print("\nError: Something unidentified went wrong, try again next time.\n")
        speedingTicket()

speedingTicket()

#
# These next two functions are for an archery program.
# Shooting is used by the archery "main()" function.
#   input: none
#   output: Graphical arrow and distance to center
#

def shooting(win):
    # Get point at which user clicks
    p = win.getMouse()
    # Set x to x coordinate of that point
    x = p.getX()
    # Set y to y coordinate of that point
    y = p.getY()

    # Head of arrow
    arrowHead = Polygon(p,Point(x-.35,y-.6),Point(x+.35,y-.6))
    arrowHead.setFill('white')
    arrowHead.draw(win)
    
    # Shaft of arrow
    arrowShaft = Line(Point(x,y-.6),Point(x,p.y-1.4))
    arrowShaft.draw(win)
    
    # Left fletch
    leftFletch = Polygon(Point(x,y-1),Point(x-.3,y-1.35),Point(x-.3,y-1.75),Point(x,y-1.4))
    leftFletch.setFill('red')
    leftFletch.draw(win)
    
    # Right fletch
    rightFletch = Polygon(Point(x,y-1),Point(x+.3,y-1.35),Point(x+.3,y-1.75),Point(x,y-1.4))
    rightFletch.setFill('red')
    rightFletch.draw(win)

    # Distance between point clicked and the center of the coordinate system.
    # The center of all my circles happens to be at 0,0.
    dist = sqrt(((x)**2) + ((y)**2))

    return dist

#
# archery() is the "main()" function of the Archery program.
#   input: none
#

def archery():

    # Define window
    win = GraphWin("Archery", 600,600)
    win.setBackground(color_rgb(9,94,0))
    win.setCoords(-10,-10,10,10)

    # Stand
    midLeg = Polygon(Point(-.75,-2.2),Point(.75,-2.2),Point(.4,-8.7),Point(-.4,-8.7))
    midLeg.setFill(color_rgb(92,0,2))
    midLeg.draw(win)

    #leftSupp = Polygon(Point(-2.2,-6),Point(-2.3,-6.5),Point(-.42,-6.7),Point(-.43,-6.35))
    #leftSupp.setFill(color_rgb(92,0,2))
    #leftSupp.draw(win)

    #rightSupp = Polygon(Point(2.2,-6),Point(2.3,-6.5),Point(.42,-6.7),Point(.43,-6.35))
    #rightSupp.setFill(color_rgb(92,0,2))
    #rightSupp.draw(win)

    leftLeg = Polygon(Point(-.8,-2.2),Point(-2.2,-2.2),Point(-4.2,-9.5),Point(-2.8,-9.5))
    leftLeg.setFill(color_rgb(92,0,2))
    leftLeg.draw(win)

    rightLeg = Polygon(Point(.8,-2.2),Point(2.2,-2.2),Point(4.2,-9.5),Point(2.8,-9.5))
    rightLeg.setFill(color_rgb(92,0,2))
    rightLeg.draw(win)
                    
    # Target
    # White circle
    wC = Circle(Point(0,0),5)
    wC.setFill('white')
    wC.draw(win)
    # Black circle
    kC = Circle(Point(0,0),4)
    kC.setFill('black')
    kC.draw(win)
    # Blue circle
    bC = Circle(Point(0,0),3)
    bC.setFill(color_rgb(44,60,242))
    bC.draw(win)
    # Red circle
    rC = Circle(Point(0,0),2)
    rC.setFill(color_rgb(227,14,14))
    rC.draw(win)
    # Yellow circle
    yC = Circle(Point(0,0),1)
    yC.setFill(color_rgb(227,227,48))
    yC.draw(win)
    # Center dot
    C = Circle(Point(0,0),.05)
    C.setFill('black')
    C.draw(win)

    # Boxes
    # Left box
    textBox1 = Rectangle(Point(-8.5,6.5),Point(-4,8.5))
    textBox1.setFill(color_rgb(232,229,149))
    textBox1.draw(win)
    # Middle box
    textBox2 = Rectangle(Point(-2,6.5),Point(2,8.5))
    textBox2.setFill(color_rgb(232,229,149))
    textBox2.draw(win)
    # Right box
    textBox3 = Rectangle(Point(8.5,6.5),Point(4,8.5))
    textBox3.setFill(color_rgb(232,229,149))
    textBox3.draw(win)

    # Drawing gridlines in the box
    x = 7.6
    for i in range(4):
        l = Line(Point(x,8.5),Point(x,6.5))
        l.draw(win)
        x = x - .9

    # Drawing "round" numbers in the scoring box
    number = 1
    x = 4.45
    for i in range(5):
        num = Text(Point(x,8), str(number))
        num.setSize(13)
        num.setStyle('bold')
        x = x + .9
        number = number + 1
        num.draw(win)

    # Dividing the box into two halves
    gridLine = Line(Point(4,7.5),Point(8.5,7.5))
    gridLine.draw(win)
    
    # Instruction box        
    boxText = Text(Point(-6.25,7.5), "Click to shoot arrows")
    boxText.draw(win)
    
    # Total score box
    scoreText = Text(Point(-.75,7.5), "Total score:")
    scoreText.draw(win)

    # Shooting arrows and scoring
    totalScore = 0
    indivScore = 0
    x = 4.45
    totalScorePrint = Text(Point(1.15,7.5),"")
    totalScorePrint.draw(win)

    # Shooting 5 arrows
    for i in range(5):
        indivScore = 0

        # This statement does two things:
        # The shooting function visually displays the arrow, but will also
        # return a value giving the distance between the point clicked and the
        # origin, or in this case, the center of the bullseye.
        dist = shooting(win)

        totalScorePrint.undraw()

        # Because radius is constant throughout a circle, the dist between the
        # arrow and the center will be able to tell what circle it is in.
        # Will show what circle and score accordingly.
        if dist >=0 and dist<1:
            totalScore = totalScore + 9
            indivScore = 9
        elif dist>=1 and dist<2:
            totalScore = totalScore + 7
            indivScore = 7
        elif dist>=2 and dist<3:
            totalScore = totalScore + 5
            indivScore = 5
        elif dist>=3 and dist<4:
            totalScore = totalScore + 3
            indivScore = 3
        elif dist>=4 and dist<5:
            totalScore = totalScore + 1
            indivScore = 1
        else:
            totalScore = totalScore + 0
            indivScore = 0

        # Printing each round's score in scoreboard
        scoreCell = Text(Point(x,7),str(indivScore))
        scoreCell.draw(win)
        x = x + .9

        # Printing total score in other scoreboard
        totalScorePrint = Text(Point(1.1,7.5),str(totalScore))
        totalScorePrint.setSize(20)
        totalScorePrint.draw(win)

    # Closing prompt
    closeText = Text(Point(-7.7,-9.5),"Click again to close...")
    closeText.setSize(10)
    closeText.draw(win)
    
    win.getMouse()
    win.close()

archery()


#
# This group of functions serve as a calendar utility.
#

#
# Leap Year will calculate if a year is a leap year.
#    input: n - "year"
#    output: 0 or 1d 

def leapYear(n):
    # In this function, result = 0 means that it is not a leap year.
    #                   result = 1 means that it IS a leap year.
    if n < 0:
        result = 0
    # If divisible by 4
    if n/4 == int(n/4):
        # If not divisible by 100
        if n/100 != int(n/100):
            result = 1
        # If divisible by 100, it's a century year
        elif n/100 == int(n/100):
            # If century year is divisible by 400 then it's a leap year
            if n/400 == int(n/400):
                result = 1
            # If century year is not divisible by 400 then it isn't a leap year
            elif n/400 != int(n/400):
                result = 0
    else:
        result = 0
        
    return result

#
# dayNumber will calculate what day of the year a date is.
#   input: date in mm/dd/yyyy
#   output: dayNumb
#


def dayNumber(n):
    # Split n by /'s
    n = str(n)
    n = n.split("/")

    # m = Month number
    m = int(n[0])
    # d = Day number
    d = int(n[1])
    # y = Year number
    y = int(n[2])

    # Define dayNumb before if statement
    dayNumb = 0

    # All possible date values
    if m >= 1 and m <= 12 and d >= 1 and d <=31 and y >= 0:
        # Uses leapYear to determine if a leap year or not
        if leapYear(y) == 0:
            # Eliminates dates that don't exist. Ex. November 31'st.
            if (m == 4 or m == 6 or m == 9 or m == 11) and (d == 31):
                dayNumb = str("That date does not exist.")
            # 2/29 does not exist in a non-leapyear.
            elif m == 2 and d == 29:
                dayNumb = str("You did not enter a date that exists within the given year.")
            # If January or February
            elif m == 1 or m == 2:
                # Formula
                dayNumb = 31*(m-1) + d
            # Months besides January or February
            else:
                x = (4*m + 23)//10
                dayNumb = 31*(m-1) + d - x

        # If it is a leap year
        if leapYear(y) == 1:
            # Still eliminating dates that don't exist
            if (m == 4 or m == 6 or m == 9 or m == 11) and (d == 31):
                dayNumb = str("That date does not exist.")
            elif m == 1 or m == 2:
                dayNumb = 31*(m-1) + d
            # If it is past Feb, you have to add a day to account for the leap day.
            else:
                x = (4*m + 23)//10
                dayNumb = (31*(m-1) + d - x) + 1
                
    # Accounting for errors
    else:
        dayNumb = str("An error occured with your input. Try again with valid calendar numbers.")

    return dayNumb
    
#
# This function will calculate when easter is in a given year from 1900-2099.
#   input: year
#   output: date of easter
#

def easter(n):

    # Forumla for Easter
    a = n%19
    b = n%4
    c = n%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    
    # Exceptions to formula
    if n == 1954 or n == 1981 or n == 2049 or n == 2076:
        # Need to subtract 7 days if these years
        easterDate = 22 + d + e - 7
    # Using formula to account for easter date
    else:
        easterDate = 22 + d + e

    # This condition makes sure it's a valid day of the month    
    if easterDate >= 1 and easterDate <= 31:
        easterDate = "March " + str(easterDate)
    elif easterDate > 31:
        # Account for if Easter date is past 31, and Easter can't be in May
        easterDate = "April " + str(easterDate - 31)

    return easterDate
        
#
# Main is a Calendar utility that combines all three prior functions.
#   input: none
#

def main():
    try:
        # Menu options, 1, 2, and 3
        print("1) Leap Year\n2) Day Number\n3) Easter")
        option = eval(input("Enter the number for the utility you wish to use: "))

        # Leap Year
        if option==1:
            n = eval(input("What year would you like to check? "))
            if n != int(n):
                print("\nDecimal years aren't allowed.\n")
                print("Try again:")
                main()
            result = leapYear(n)
            # 0 = not leap year
            if result == 0:
                print(str(n), "is not a leap year.")
            # 1 = leap year
            elif result == 1:
                print(str(n), "is a leap year.")

        # Day Number
        elif option==2:
            n = input("Enter a date in the form of month/day/year. ")
            result = dayNumber(n)
            # The reason str and int work is because my error strings within dayNumber are
            # strings. Any successful operation results in an int.
            if type(result) == str:
                print(result)
            # Success = int
            elif type(result) == int:
                print("The date you entered is day", result, "in that year.")

        # Easter
        elif option==3:
            n = eval(input("Enter a year from 1900-2099 to find the date of Easter in that year. "))
            # Must be within these years
            if n >= 1900 and n <= 2099 and n == int(n):
                result = easter(n)
                print("Easter is on", result, "in", n)
                
            else:
                print("\nInvalid input.\n")
                print("Try again:")
                main()
                     
        else:
            print("\nYour number exceeded the range of the options available.\n")
            print("Try again:")
            main()

    # Excepts for errors
    except NameError:
        print("\nError: You did not enter a number.\n")
        print("Try again:")
        main()
    except SyntaxError:
        print("\nError: Your input format was wrong.\n")
        print("Try again:")
        main()
    except TypeError:
        print("\nYou did not enter a number.\n")
        print("Try again:")
        main()
    except ValueError:
        print("\nError: You did not enter a valid number value.\n")
        print("Try again:")
        main()
    except:
        print("\nError: Something else unidentified went wrong, try again.")
        print("Try again:")
        main()

main()

