#
# HW10Prob2
#
# Austin Chen
#
# This module contains problem #2 for Homework #10.
#

#
# This function will take the list that was read from the file and remove all \n's from the string.
#   input: strList
#

def removeEndLine(strList):
    
    # Split the string by \n
    strList = strList.split("\n")
    # Chop off the unnecessary empty index at the end
    strList = strList[0:(len(strList)-1)]

    return strList

#
# This function will take the new strList and convert each index to an integer.
#   input: strList
#

def toNumbers(strList):

    # Create a blank list called 'newList'
    newList = []
    # Will loop through each index in the list 'strList'
    for i in strList:
        # Change each str into an int
        i = int(i)
        # Append the new int to the list called 'newList'
        newList.append(i)
        
    return newList

#
# This function will square each integer value within the list 'strList'.
#   input: strList
#
        
def squareEach(strList):
    # Create a blank list called 'newList'
    newList = []
    # Will loop through each index in the list 'strList'
    for i in strList:
        # Squaring each index value
        i = i * i
        # Append the resulting new int to the list 'newList'
        newList.append(i)
        
    return newList

#
# This function will create a sum of all squared numbers from the previous function.
#   input: strList
#

def sumList(strList):
    # Start with 'totalNumb' equal to 0
    totalNumb = 0
    # Will loop through each index value within 'strList'
    for i in strList:
        # Add specific index value to totalNumb each iteration
        totalNumb = totalNumb + i

    return totalNumb
        
# Main function will combine all aforementioned functions.
# Main will ask for a file input of numbers
# Numbers will be squared and summed. Output will be printed to a new file.

def main():
    # Gathering user input
    userFile = input("Enter the name of the file to use as input: ")
    outFile = input("Enter a name for the output file: ")

    # Read and write files
    outFile = open(outFile, "w")
    inFile = open(userFile, "r")

    # Set strList to the contents of the document
    strList = inFile.read()

    # Use the removeEndLine function to remove every \n from the string.
    # Note: strList will be redefined each time it is used as an input to the functions below.
    strList = removeEndLine(strList)

    # Use the 'toNumbers' function to convert each index into a string.
    strList = toNumbers(strList)
    # Will save this new iteration of strList into a seperate value to be called later.
    # This is because strList will continue to be modified as main() continues.
    numList = strList
    
    # Use the 'strList' function to square each index value.
    strList = squareEach(strList)
    
    # Use the 'squareSum' function to sum each index value in strList.
    # Output is saved in returned variable squareSum.
    squareSum = sumList(strList)
    
    
    # Text format for output file

    # First line
    firstLine = "The square of each term is: "
    print(firstLine, file=outFile)

    # The middle lines
    # x will be recursively used to move through the list.
    x = 0
    # Will loop for every index in the list.
    for i in range((len(strList))):
        # Starts at the 0th index in numList
        print(numList[x],end="", file=outFile)
        # Formatting
        print("^2 = ",end="", file=outFile)
        # strList can also use x because strList and numList are aligned in corresponding values.
        print(strList[x], file=outFile)
        # Recursive x modifier
        x = x + 1
    print("", file=outFile)

    # Last line
    # squareSum is assigned via the sumList function above.
    lastLine = "The sum of the squares is " + str(squareSum)
    print(lastLine, file=outFile)
    
    #Closing the files
    inFile.close()
    outFile.close()
    
    # Feedback
    print("Your file has been created.")


main()
    
