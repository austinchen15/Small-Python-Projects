#
#HW09
#
#Austin Chen
#
#This module contains problems 1-4 for Homework #9.
#

from graphics import *
import math

#
#This function will convert user input into camel case.
#   input: none
#

def camelCase():
    print("Camel Case")
    #User will input a phrase to be stored in userInput
    userInput = input("Enter a non-numerical phrase to be converted into camel case: ")
    #This will split the user's input to a list with each space seperating a part of the index
    userInput = userInput.split(" ")

    #Creates a new list variable of the first index in userInput
    firstWord = userInput[0]
    #Converts all letters to lowercase
    firstWord = firstWord.lower()
    #Slices string down to only the 0th index, or 1st value.
    firstWord = firstWord[0]
    #Prints value, end="" to keep on the same line
    print(firstWord,end="")

    #Creates a list of all words after the first
    otherWords = userInput[1:]
    #Used for increasing the amount of letters used in subsequent words
    x = 2
    #For "word" in list of otherWords
    for word in otherWords:
        #Capitalize the word
        word = word.capitalize()
        #Slice the word, x will start at 2 and rise by 1 to allow more letters in each subsequent word
        word = word[0:x]
        #Print the newly formatted word
        print(word,end="")
        #x modifier
        x = x + 1

    print("")
    print("")

camelCase()



#
#This function will use a Caesar cipher to read a message and key, then save the encoded message and a
#decoding key to a different text file.
#   input: none
#

def caesar():

    print("Caesar Cipher")
    
    #Alphabet string to use
    aBet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Name the input and output files
    userFile = input("Enter the text file name with the extension .txt: ")
    outFile = input("Enter a name for the file containing the encoded message and decoding key. Use extension .txt: ")
    outFile = open(outFile, "w")

    #Read the input file
    inFile = open(userFile, "r")
    #Read the entire file, assign to openedFile
    openedFile = inFile.read()
    #Split file by \n
    splitFile = openedFile.split("\n")
    #Will be separated into two variables: message and key
    message = splitFile[0]
    key = eval(splitFile[1])
    
    #Assignment to stuff before ForLoop
    letterIndex = 0
    shiftedLetterIndex = 0
    finalMessage = ""
    

    #ForLoop will go through each character in the message
    for i in message:
        #For each letter, find the index value within the Alphabet string.
        letterIndex = aBet.find(i)
        #Shift the letter by key. Key%52 so that the shift exists (so for like 700 it will still work)
        shiftedLetterIndex = letterIndex - (key%52)
        #Add the shifted letter to the final message
        finalMessage = finalMessage + (aBet[shiftedLetterIndex])

    #The decoding key is the length of my alphabet list - key. It will create a value to loop back around the string.
    decodingKey = 53 - key        

    #Output file text
    #I originally had a bunch of instructions on how to decode before I figured out how to get a decoding value
    #So I left it here but did not print it in the document.
    decodingKey1 = "Alphabet index: ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' "
    decodingKey2 = "Index values:   '0123456789...........................................' "
    decodingKey3 = "The original phrase was shifted " + str((key%52)) + " index value(s) to the left to produce message in the first line."
    decodingKey4 = "To decode, look at the Alphabet index. Locate letter to decode, and move " + str((key%52)) + " space(s) to the"
    decodingKey5 = "right. Loop around to the beginning of the index if necessary."
    decodingKey6 = "Tip: click in front of the letter to decode. For example, |J. Press your right arrow key " + str((key%52))
    decodingKey7 = "times, and your decoded letter will be in front of your | cursor. Make sure to loop around when necessary."
    decodingKey8 = "Decoding Key: " + str(decodingKey)

    #Output file print
    print(finalMessage, file=outFile)
    #print("", file=outFile)
    #print(decodingKey1, file=outFile)
    #print(decodingKey2, file=outFile)
    #print(decodingKey3, file=outFile)
    #print("", file=outFile)
    #print(decodingKey4, file=outFile)
    #print(decodingKey5, file=outFile)
    #print(decodingKey6, file=outFile)
    #print(decodingKey7, file=outFile)
    print("", file=outFile)
    print(decodingKey8, file=outFile)
    
    #Close files
    inFile.close()
    outFile.close()

    print("Done")

    print("")

caesar()



#
#This function will create a horizontal chart of student class averages.
#   input: none
#


def grades():

    print("Grades")
    #Read the file, split the data by lines
    fileName = input("What text file should I read the grades from? ")
    openedFile = open(fileName,"r")
    rawData = openedFile.read()
    slicedData = rawData.split("\n")

    #Create window size and coordinate plane
    window = GraphWin("Grades", 700, 500)
    window.setCoords(0,0,100,100)

    #Will be used to calculate the numbers to use for the bars and how many times to loop
    #Uses the raw data
    space = 90/len(slicedData)
    loops = len(slicedData)

    #x assignment before ForLoop
    x = 0

    #ForLoop will loop "loops"-1. I'm not sure why -1, but it fixed my problems
    # My original problem was that when I got to the last iteration, firstSplit didn't
    # have anything in it and therefore mod2 would be unhappy and spit out red error text.
    for i in range(loops-1):
        slicedDataIndex = slicedData[i]
        firstSplit = slicedDataIndex.split(" ")

        #Will create seperate variables for indices 0 and 1 in firstSplit
        mod1 = firstSplit[0]
        mod2 = eval(firstSplit[1])

        #Labeling the bar
        p1 = Point(5,85-x)
        initials = Text(p1,"{0:3}".format(mod1))
        initials.draw(window)

        #Drawing the bar
        bar = Rectangle(Point(10,80-x),Point(mod2, 90-x))
        bar.draw(window)
        fill = Text(Point(mod2/2, 85-x),"{0:0.1f}%".format(mod2))
        fill.draw(window)

    
        x = x + space

    #Click to close window
    window.getMouse()
    window.close()
    
    print("")

grades()


    
#
#This function will calculate compound interest.
#   input: none
#

def interest():
    print("Interest Calculator")
    #Input for all four variables to use in equation
    principal = eval(input("Enter amount of investment: "))
    interest = eval(input("Enter annual interest rate as decimal: "))
    compoundRate = eval(input("Enter how many times to compound a year: "))
    compoundLength = eval(input("Enter how many years on the investment: "))

    #Format of the top of the table
    print()
    yearsAmount = "Year       Investment"
    print("{0}".format(yearsAmount))
    space = "      "
    line1 = ("-----------------------")
    print("{0}".format(line1))

    #ForLoop will repeat how many years + 1 times
    for i in range(compoundLength+1):
        print(i,"         ${0:0.2f}".format(principal))
        #Equation for compound interest. It excludes the t because the forloop will repeat each time.
        # Repetitions of the forloop will show intermediate years of compounding
        principal = round(principal*((1+(interest/compoundRate))**(compoundRate)),2)
    print("")
        

interest()


    
                     

    
    
    
    



