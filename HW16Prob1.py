#
# HW #13
#
# Austin Chen
#
# This module contains problem one for HW16.
#


#
# This function contains an insertionSort sorting algorithm.
#   input: list
#

# Insertion sort is inefficient on large lists but is short and simple.
def insertionSort(x):

    # Loops len(x) - 1 times)
    for i in range(1,len(x)):
        # Assigns new variable y to 2nd index in x
        y = x[i]

        # Acts as a counter and is used for list comparisons
        z = i

        while z > 0 and y < x[z-1]:
            # Compares the current item to the list item before it
            x[z] = x[z-1]
            # Counts down
            z = z - 1

        # Sets new list
        x[z] = y
    return x



#
# This function contains a quickSort sorting algorithm.
#   input: list
#

# Quick sort is efficient because it's systematic with comparisons. More efficient than insertion sort.


def quickSort(x):
    # Defining 3 placement lists
    lower = []
    same = []
    higher = []

    # If the list has more than 1 index
    if len(x) > 1:
        # Set the pivot to the first item on the list
        pivot = x[0]
        # Loops for each index value in list x
        for i in x:
            # If i is bigger than the pivot value, then put in lower list
            if i < pivot: lower.append(i)
            # If i is the same, put it in the same list
            if i == pivot: same.append(i)
            # If i is greater, then put it into the higher list.
            if i > pivot: higher.append(i)
        # Returning in this order gives a sorted representation of the list.
        return quickSort(lower) + same + quickSort(higher)
    
    # If the length is not greater than 1, then there should be nothing to sort.
    else:
        return x           

#
# This function contains a bubbleSort sorting algorithm.
#   input: list
#

# Bubble sort is as efficient as quick sort, if not a little bit more efficient.
# Instead of spitting out a new list, it's just going to modify the original 'x' list.

def bubbleSort(x):

    # Priming read
    isSorted = False

    while isSorted == False:

        # Assume you've sorted it at the beginning, but once you hit the ForLoop,
        # the code will assume it's False if anything is out of order.
        isSorted = True

        # Will loop for the length of the list - 1
        for i in range(int(len(x)-1)):
            # If the first index is larger than the one next to it, the list isn't sorted.
            if x[i] > x[int(i+1)]:
                isSorted = False
                # Needs to rearrange, so set z to the item that's smaller
                z = x[int(i+1)]
                # Rearranging values
                x[int(i+1)] = x[i]
                x[i] = z

    return x





















    
