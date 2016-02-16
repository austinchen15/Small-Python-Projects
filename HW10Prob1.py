#
# HW10Prob1
#
# Austin Chen
#
# This module contains problem #1 for Homework #10.
#

#
# This program will print up to four verses of mary had a little lamb.
#

#
# This function is a repeated phrase for the verse.
# Input: none
#
def maryHad():
    print("Mary had a ", end="")

#
# This function is a repeated phrase for the verse.
# Input: none
#    
def lLamb():
    print("little lamb, ", end="")

#
# This function is a repeated phrase for the verse.
# Input: none
#
def eW():
    print("Everywhere that ", end="")

#
# This function is a repeated phrase for the verse.
# Input: none
#
def maryWent():
    print("Mary went, ", end="")
    
#
# This function is a repeated phrase for theo verse.
# Input: none
#
def followed():
    print("It followed her to ", end="")

    
#
# This function is a repeated phrase for the verse.
# Input: none
#
def toSchool():
    print("school one day, ", end="")

#
# This function is a repeated phrase for the verse.
# Input: none
#
def itMade():
    print("It made the children ", end="")
    
#
# This function is a repeated phrase for the verse.
# Input: none
#
def lP():
    print("laugh and play, ", end="")

#
# This function will use previous functions to construct and print the first verse.
# Input: none
#    
def firstVerse():
    maryHad()
    lLamb()
    print()
    lLamb()
    lLamb()
    print()
    maryHad()
    lLamb()
    print()
    print("whose fleece was white as snow.")

#
# This function will use previous functions to construct and print the second verse.
# Input: none
#  
def secondVerse():
    eW()
    maryWent()
    print()
    maryWent()
    maryWent()
    print()
    eW()
    maryWent()
    print()
    print("the lamb was sure to go.")

#
# This function will use previous functions to construct and print the third verse.
# Input: none
#  
def thirdVerse():
    followed()
    toSchool()
    print()
    toSchool()
    toSchool()
    print()
    followed()
    toSchool()
    print()
    print("which was against the rules.")

#
# This function will use previous functions to construct and print the fourth verse.
# Input: none
#  
def fourthVerse():
    itMade()
    lP()
    print()
    lP()
    lP()
    print()
    itMade()
    lP()
    print()
    print("to see a lamb at school.")
    
#
# This function will choose the amount of verses to display.
# Input: n verses
#      
def allVerses(n):
    # Create a list of every function
    x = [firstVerse,secondVerse,thirdVerse,fourthVerse]
    # Y will be used within the ForLoop to progress each verse.
    y = 0
    # range(n) will grab "n" input from main() input. N will decide how many verses to display.
    for i in range(n):
        # Line spacing
        print()
        #Print verse with index y
        (x[y])()
        # Line spacing
        print()
        y = y + 1

#    
# This is the main function of the program. Will use parts from each previous function to
# print a user specified number of verses from "Mary Had a Little Lamb"
#

def main():
    n = eval(input("How many verses of 'Mary Had a Little Lamb' do you want? "))
    allVerses(n)

main()
    
