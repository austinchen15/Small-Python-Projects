from graphics import *

class GraphicsGroup:
    
    def __init__(self, anchor):
        self.anchor = [anchor]

    def getAnchor(self):
        return self.anchor[0].clone()
    
    def addObject(self, graphicsObject):
        self.anchor.append(self.graphicsObject)

    def move(self,dx,dy):
        self.anchor.move(dx,dy)

    def draw(self,win):
        for i in range(1,len(self.anchor)-1):
            i.draw(win)
            
        self.anchor.draw(win)

    def undraw(self,win):
        for i in self.anchor:
            i.undraw()

    def __str__(self):
        cardName = []
        for i in self.anchor:
            cardName.append(str(i))
        return ", ".join(cardName)

def main():
    input = 
    
