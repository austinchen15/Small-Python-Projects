#
# HW12
#
# Austin Chen
#
# This module contains homework problems 1-3 for HW12.
#

from graphics import *
import random
import time
import math

#
# This function will convert a picture to greyscale.
#   input: none
#

def greyscale():
    try:
        # File input for image
        pic = input("Filename of photo to import: ")
        # Naming the output, saving as variable
        outName = input("Enter name for output file: ")

        # Assigning imported image as Image 
        file = Image(Point(0,0),pic)

        # X and Y coordinate lengths of picture
        x = file.getWidth()
        y = file.getHeight()
        
        # Create graphics window
        win = GraphWin("Greyscale",x,int(y+120))
        
        # Draw picture in window
        file = Image(Point(x/2,((y/2)+120)), pic)
        file.draw(win)

        # Instructions prompt
        prompt = Text(Point(x/2,65),"Click again for greyscale.")
        prompt.setSize(12)
        prompt.setFace('courier')
        prompt.draw(win)

        # Pause, wait for mouse click to continue
        win.getMouse()
        prompt.undraw()
        
        # n and n are 0's because x and y are already assigned as width and height.
        n = 0
        m = 0

        # Will loop as many times as there are pixels in the picture.
        for i in range(x*y):
            # Grabs the color of 1 pixel, stores it in a list
            pix = file.getPixel(int(n),int(m))

            # Changing the color based on colors in list previously defined
            r = pix[0]
            g = pix[1]
            b = pix[2]
            a = int(0.3*r + 0.6*g + 0.1*b)

            # Set pixel color to greyscale
            file.setPixel(int(n),int(m),color_rgb(a,a,a))

            # Moves n to the next pixel to the right
            n = n + 1
            # When n reaches the end of the row, which is as many pixels as there are in the picture,
            # n will reset to 0, effectively bringing it back to the left. Pixel changer will drop down
            # a row as well and update the frame to show transition.
            if n == int(x):
                n = 0
                m = m + 1
                win.update()
        # Saving the completed file as a pic
        file.save(outName)

        # Exit prompt
        outText = Text(Point(x/2,65), "Click again to close.")
        outText.setSize(12)
        outText.setFace('courier')
        outText.draw(win)

        # Pause for mouse click
        win.getMouse()
        win.close()

        # Shell feedback for function completion
        print("Done")
    except NameError:
        print("\nSomething went wrong, try again.")
        greyscale()
    except SyntaxError:
        print("\nSomething went wrong, try again.")
        greyscale()
    except TypeError:
        print("\nSomething went wrong, try again.")
        greyscale()
    except ValueError:
        print("\nSomething went wrong, try again.")
        greyscale()

greyscale()
        

#
# This function will allow users to play the game "Nim".
#   input: none
#

def nim():
    try:
        # Introduction and instructions
        print("Nim")
        print("Players alternate taking 1 or 2 sticks from the pile.")
        print("Whoever clears the pile loses the game.")
        print()
        
        
        # List of common strings to be used later in the program
        p1Prompt = "\nPlayer 1: How many sticks do you want to take? "
        p2Prompt = "\nPlayer 2: How many sticks do you want to take? "
        p1Win = "\nPlayer 2 picked up the last stick so Player 1 wins!"
        p2Win = "\nPlayer 1 picked up the last stick so Player 2 wins!"
        error1 = "That was not a valid option (pick up either 1 or 2 sticks)."
        #error2 = "start over:\n"
        error3 = "There is only 1 stick left. You can't pick up 2. Try again:\n"
        error4 = "\nInvalid input. Try again: \n"

        # Setting up the rules of the game, such as how many sticks to use total
        numSticks = eval(input("Number of sticks to use: "))
        # Error catching, can't enter a negative number of sticks
        if numSticks < 0:
            print(error4)
            nim()

        # Turn and sticks taken start at 0 and will be reassigned later.
        # The number of sticks left = how many sticks the user defined at the
        # beginning of the game.
        turn = 0
        sticksTaken = 0
        sticksLeft = numSticks

        # Will run if there are sticks left (not 0).
        while sticksLeft >=1:
            
            # The turn variable will oscillate between integers 0 and 1.
            # At the end of each turn, the turn is switched back to either 0 or 1.
            if turn == 0:
                # Gathering user input for how many sticks P1 will take.
                sticksTaken = eval(input(p1Prompt))
                # Error catching for picking up 2 sticks when only 1 is left
                if sticksTaken == 2 and sticksLeft == 1:
                    print(error3)
                # Further error catching for taking an invalid number of sticks
                elif sticksTaken == int(sticksTaken) and sticksTaken >=1 and sticksTaken <=2:
                    # After taking sticks, turn will switch to the other player's turn
                    turn = 1
                    # Subtracts from the total number of sticks provided at the beginning
                    sticksLeft = sticksLeft - sticksTaken
                    # Displays how many sticks are left
                    print("There are", sticksLeft, "sticks left.")
                    # Breaks from the loop if number of sticks left = 0
                    if sticksLeft == 0: break
                else: print(error1)

            # Same brick of text, only differnce being prompts customized for one player or the other.
            # The comments from above apply.
            if turn == 1:
                sticksTaken = eval(input(p2Prompt))
                if sticksTaken == 2 and sticksLeft == 1:
                    print(error3)   
                elif sticksTaken == int(sticksTaken) and sticksTaken >=1 and sticksTaken <=2:
                    turn = 0
                    sticksLeft = sticksLeft - sticksTaken
                    print("There are", sticksLeft, "sticks left.")
                    if sticksLeft == 0: break
                else: print(error1)

        # After sticksLeft == 0, the while loop should break and send the program
        # into post-game feedback. If the game ended on turn 0, p1 won. Vice versa.
        if turn == 0: print(p1Win)
        if turn == 1: print(p2Win)
        
    except NameError:
        print("\nSomething went wrong, try again.")
        nim()
    except SyntaxError:
        print("\nSomething went wrong, try again.")
        nim()
    except TypeError:
        print("\nSomething went wrong, try again.")
        nim()
    except ValueError:
        print("\nSomething went wrong, try again.")
        nim
        ()

nim()

#
# This function will calculate total loan values and the number of months it will take to pay.
#   input: none
#
def loanCalculator():
    try:
        # Welcome statement
        print("\nWelcome to the Loan Calculator!")

        
        #Defining variables to use in math equations and such
        # q to quit string
        q = "p"
        

        # Simple counter variable to count up in nested while loop
        mont = 0

        # If q = anything else besides q, it will keep running.
        # Once the user enters q to quit, the while loop will end.
        while q != "q":

            # Amount borrowed
            aB = 0
            # Interest rate
            apr = 0
            # Monthly payment
            mP = 0

            # How much time it will take to pay off loan
            timePay = 0
            # Total amount
            tA = 0
            # Months
            mont = 0

            # Input gathering and error catching
            aB = eval(input("Amount borrowed ($): "))
            
            if (type(aB)!= int) and type(aB) != float or (aB <=0):
                print("\nInvalid input, try again:\n")
                loanCalculator()
                
            apr = eval(input("Annual interest rate (decimal): "))/12
            if type(apr) != float or apr <= 0:
                print("\nInvalid input, try again:\n")
                loanCalculator()
                
            mP = eval(input("Monthly payment ($): "))
            if type(mP) != int and type(mP)!= float or mP <= 0: 
                print("\nInvalid input, try again:\n")
                loanCalculator()


            # Equation for calculating the amount total and months to pay
            # The way this loop works is that it will run through time, simulating
            # each period to gather total balance.

            # It will run until amount borrowed reaches 0.
            while aB >= 0:

                # Increase counter by 1 each loop
                mont = mont + 1
                # Equation forcalculation
                aB = (aB * (1 + apr)) - mP

            # Total amount, given aB at the end of the loop
            tA = mP * (mont-1) + mP + aB

            # Result text
            print("     \nYou will fully pay off the loan in",  mont, "months.")
            print("     \nIn total, you will pay $",round(tA,2))

            # Exit query
            q = input("\nEnter 'q' to quit, hit any other key to run again. ")
            print()

        # Exit prompt
        exit = "\nThanks for using the Loan Calculator!!!!!!!!!!!"
        for i in exit:
            print(i,end="")
            time.sleep(.035)
    except NameError:
        print("\nSomething went wrong, try again.")
        loanCalculator()
    except SyntaxError:
        print("\nSomething went wrong, try again.")
        loanCalculator()
    except TypeError:
        print("\nSomething went wrong, try again.")
        loanCalculator()
    except ValueError:
        print("\nSomething went wrong, try again.")
        loanCalculator()
        
        
        
loanCalculator()    


