#
#HW06
#
#Austin Chen
#
#This module contains homework questions 1-4.
#


import time

#
#This function will calculate the average of a set of scores for a user.
#   input: none
#
def averageScore():

    #This explains the function's purpose.
    print("This function will calculate the average of your test scores.")

    #numberOfScores will be given an input on how many test scores to average.
    #This value will be used as the upper bound for the ForLoop.
    numberOfScores = eval(input("How many test scores do you have to average?"))

    #This is the total of all scores. Each time the program is re-run, the total is set to 0.
    total = 0

    #This loop will repeat numberOfScores times, each time asking for a score.
    for i in range(numberOfScores):
        testScores = eval(input("Enter score: "))

        #Total keep track of a combined sum of all the testScores so far.
        total = total + testScores

    #total/numberOfScores is the formula for the average. The program will then print the average.
    print("The average of these scores is", total/numberOfScores)




#
#This function will convert a set of lengths in feet to a set of lengths in inches.
#   input: none
#                           
def convert():
    print("This function will convert a set of lengths measured in feet to inches.")

    #Asks the user for an input in feet. User is asked to input a list.
    lengths = eval(input("Enter a list of lengths in feet"))

    #Conversion print statement
    print("Those lengths of feet in inches are [", end=" ")

    #This will take the list the user input. For each index in the list, ForLoop will convert and then print.
    for i in lengths:
        feet = i*12
        print(feet, end=" ")

    print("]")



#
#This function will calculate the average of a set of scores for a user.
#   input: none
#
def countdown():
    print("This function will count up to a number and then count back down.")

    #This input will ask the user for a number to count up to
    number = eval(input("What number would you like to count to? "))

    #This loop will then count to the number the user previously specified.
    for i in range(number):
        print(i)
        time.sleep(.15)

    #This loop counts down from that number back to 1
    for i in range(number):
        print(number-i)
        time.sleep(.15)

    print("0")



#
#This function will use the recursive definition to print triangular numbers up to "n".
#   input: integer greater than or equal to 0.
#
def triangle(n):

    #Initial value for X.
    x = 0

    #This ForLoop will calculae and print the triangular numbers.
    for i in range(n+1):
        x=x+i
        end = print(x, end=", ")

        
