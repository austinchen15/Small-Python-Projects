#
# HW15
# 
# Austin Chen
#
# This module contains the main function for homework problem #3.
#

import random
from graphics import *

class Card:

    def __init__(self,value,suit):
        """Creates a card class which will define card objects as a value and a suit"""
        self.value = value
        self.suit = suit
        self.Vis = []
        self.dispValue = []
        
    def getValue(self):
        """ Returns value of card object """
        return self.value

    def getSuit(self):
        """ Returns suit of card object """
        return self.suit

    def draw(self,win,center,width,height):
        """ Draws the card given user defined parameters """
        cardVis = Rectangle(Point((center.getX()-width/2),(center.getY()-height/2)), Point((center.getX()+width/2),(center.getY()+height/2)))
        cardVis.setFill('white')

        # Card values are organized as values 2-14. The user doesn't want to see 13 for King, so this set
        # of if statements translates values to strings that can be graphically displayed on the scren.
        if self.value == 11:
            self.dispValue = "Jack"
        elif self.value == 12:
            self.dispValue = "Queen"
        elif self.value == 13:
            self.dispValue = "King"
        elif self.value == 14:
            self.dispValue = "Ace"
        else:
            self.dispValue = int(self.value)
        
        # Defining number on the card on the screen
        numVis = Text(Point(center.getX(),center.getY()-height/5), self.dispValue)
        # Defining suit on the card on the screen
        suitVis = Text(Point(center.getX(),center.getY()+(height/10)), self.suit)

        # Drawing all card components
        cardVis.draw(win)
        suitVis.draw(win)
        numVis.draw(win)

        # Creating a list of all components, this will be used for undrawing ease
        self.Vis = [cardVis, suitVis, numVis]

    def undraw(self):
        """ Undraws the card object """
        # Takes self.Vis list and undraws all components in that card
        for i in self.Vis:
            i.undraw()

    def __str__(self):
        """ Prints out a str of what the card is """
        return self.suit + " " + str(self.value)

class UnoCard(Card):
    """ Subclass of Card class but with Uno Cards """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.Vis = []
        self.dispValue = []

    def draw(self,win,center,width,height):
        """ Draws the card given user defined parameters """
        cardVis = Rectangle(Point((center.getX()-width/2),(center.getY()-height/2)), Point((center.getX()+width/2),(center.getY()+height/2)))
        cardVis.setFill('white')

        # Card values are organized as values 2-14. The user doesn't want to see 14 for Wild Draw Four, so this set
        # of if statements translates values to strings that can be graphically displayed on the scren.
        if self.value == 10:
            self.dispValue = "Skip"
            
        elif self.value == 11:
            self.dispValue = "Draw Two"
            
        elif self.value == 12:
            self.dispValue = "Reverse"
            
        elif self.value == 13:
            self.dispValue = "Wild"
            
        elif self.value == 14:
            self.dispValue = "Wild Draw \nFour"
        else:
            self.dispValue = int(self.value)
        
        # Defining number on the card on the screen
        numVis = Text(Point(center.getX(),center.getY()-height/5), self.dispValue)
        # Defining suit on the card on the screen
        suitVis = Text(Point(center.getX(),center.getY()+(height/10)), self.suit)

        # Drawing all card components
        cardVis.draw(win)
        suitVis.draw(win)
        numVis.draw(win)

        # Creating a list of all components, this will be used for undrawing ease
        self.Vis = [cardVis, suitVis, numVis]

class Deck:

    def __init__(self):
        """ Deck creates a full 52 card deck of unique card objects."""

        # Defining all card possibilities
        suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        self.deck = []

        for x in suit:
            for y in value:
                self.deck.append(UnoCard(y,x))
        
        self.cards = []
        self.cardsQ = 52

    def getTopCard(self):
        """ Will return the card object that is at the top of the deck """
        self.cardsQ = self.cardsQ - 1
        card = self.deck[0]
        self.deck = self.deck[1:]
        
        return card

    def getCardsLeft(self):
        """ Will return how many cards are left in the deck """
        return self.cardsQ

    def cutDeck(self,n):
        """ Cuts the deck in half and repositions one half after the other """
        # Because deck is a list of card objects, it can take the first specified chunk and then reverse it for the other chunk
        half1 = self.deck[:n]
        half2 = self.deck[n:]

        # Return the cut deck
        return half2 + half1
    
    def splitDeck(self, n):
        """n = 0 splits it into the first half, n = 1 splits it into the 2nd half of a static deck"""
        # Divides the deck in half that can be picked up by 2 players
        if n == 0:
            return self.deck[:26]
        elif n == 1:
            return self.deck[26:]

    def shuffle(self):
        """ Shuffles the deck """
        random.shuffle(self.deck)
        
        """ Prints out all cards in the deck """
    def __str__(self):
        cardName = []
        # Goes through each index of the deck, and spits out a giant string of all the cards in the deck
        for i in self.deck:
            cardName.append(str(i))
        return ", ".join(cardName)

class UnoDeck(Deck):
    """ Subclass of Deck """
    
    def __init__(self):
        """ Initializes a deck with 108 cards """
        value = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]
        color = ["Red", "Green", "Blue", "Yellow"]
    
        wildColor = ["Black"]
        wildValue = [13,13,13,13,14,14,14,14]

        self.deck = []

        # Create the deck
        for x in color:
            for y in value:
                self.deck.append(UnoCard(y,x))
        # Create the deck
        for v in wildColor:
            for w in wildValue:
                self.deck.append(UnoCard(w,v))
        
        self.cards = []
        self.cardsQ = 108

    
    def getActionsInFirstSevenCardsOfUnoDeck(self):
        """ That method name doe """
        
        """ Calculates how many Action cards are in the first 7 cards of the deck """ 
        x = 0
        for i in range(7):
            if int(self.deck[i].getValue()) == 10 or int(self.deck[i].getValue()) == 11 or int(self.deck[i].getValue()) == 12:
                x = x + 1
        return x

    def getWildsInFirstSevenCardsOfUnoDeck(self):
        """ That method name doe """

        """ Calculates how many Wild cards there are in the first 7 cards of the deck """
        x = 0
        for i in range(7):
            if int(self.deck[i].getValue()) == 13 or int(self.deck[i].getValue()) == 14:
                x = x + 1
        return x

#
# This main function compiles all of the classes to graphically draw 7 uno cards.
#   input: none
#

def main():
    # Creating the graphics window
    win = GraphWin("Uno Sample Hand", 600, 600)
    win.setBackground("blue")

    # Creating uno deck
    unoSet = UnoDeck()
    unoSet.shuffle()

    # Card width and height
    cW = 63.6
    cH = 90

    # Defining the center point
    centerPoint = Point(51.15, 300)

    # Drawing the hand across the screen
    for i in range(7):
        unoSet.deck[i].draw(win,centerPoint, cW, cH)
        centerPoint.move(82.95,0)
        
    # Calculates how many action and wild cards are in the first 7 cards of the deck
    actions = str(unoSet.getActionsInFirstSevenCardsOfUnoDeck())
    wilds = str(unoSet.getWildsInFirstSevenCardsOfUnoDeck())

    # Prints above information to the user
    swag1 = "There are " + actions + " action cards and " + wilds + " wild cards in your hand."
    swag2 = Text(Point(300,420), swag1)
    swag2.draw(win)

    # Closing
    win.getMouse()
    win.close()

main()       
        
        

