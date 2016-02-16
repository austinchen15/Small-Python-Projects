#
# HW16 Prob 2
#
# Austin Chen
#
# This module contains problem 2 for HW16.
#

#
# This function reverses a string.
#   input: word
#   output: word reversed
#

def reverse(word):
    # Part of the recursive function will need to stop the recursion in order to avoid
    # an infinite loop
    if len(word) == 0: return word

    # The recursive portion of this function will use the function itself in
    # reordering the string. The return statement below will take the first
    # letter off the word and add it to the end until the full string is reversed.
    else: print((reverse(word[1:]) + word[0]))

#
# This function translates numbers into strings.
#   input: number
#   output: number in strings
#

def digitsToWords(n):

    # Bank for translation
    bank = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # The function will turn n into a string in order to work with varying lengths
    nStr = str(n)

    # Similar to reverse's structure, it will take the first index and translate it
    # and digitsToWords what's left until there's nothing
    if len(nStr) == 0: return nStr
    
    else:
        # Set nRes to the string equivalent from bank
        nRes = bank[int(nStr[0])]
        print(nRes + " " + digitsToWords(nStr[1:]))
    
#
# This function determines if a subset of numbers adds up to x.
#   input: nums, x
#   output: subset of numbers or none
#

def sumToTarget(nums,x):
    if len(nums) == 0: return nums
    else: return sumToTarget(nums[1:])

def main():
    selection = True

    while selection == True:
        print()
        print("Choose an option:")
        option = eval(input("1) reverse(word)  2) digitsToWords(n)  3) sumToTarget(nums,x) 4) Quit "))

        if option == 1:
            print()
            word = input("Enter a word to reverse: ")
            reverse(word)

        elif option == 2:
            print()
            number = eval(input("Enter a number to turn into words: "))
            digitsToWords(number)

        elif option == 3:
            print()
            nums = input("Enter a list of integers: ")
            x = input("Enter a positive sum to check: ")

            sumToTarget(nums,x)

        elif opption == 4:
            break

        else: print()


