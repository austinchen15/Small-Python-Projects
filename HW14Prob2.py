
class Team:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.ties = 0
        self.losses = 0
        
    def getName(self):
        return self.name

    def getWins(self):
        return self.wins

    def getTies(self):
        return self.ties

    def getLosses(self):
        return self.losses

    def addWin(self):
        self.wins = self.getWin() + 1

    def addTie(self):
        self.ties = self.getTies() + 1

    def addLoss(self):
        self.loss = self.getLosses() + 1
        
        



def main():
    
    userFile = input("Enter filename to input: ")
    outFile = input("Enter filename of output: ")

    print("How would you like to sort the data?")
    print()
    print("1) Most wins  2) Most losses  3) Most draws")
    
    choice = eval(input(""))

    inFile = open(userFile,"r")

    league = ""
    teams = []

    league = inFile.readline()

    # Creating Team objects in list: team
    for i in range(4):
        fill = inFile.readline()
        fill = fill.rstrip()
        teams.append(Team(fill))

    # To account for the extra space
    nothing = inFile.readline()

    # Match history
    for i in range(6):
        # Strips the match history and feeds data line by line for below
        fill = inFile.readline()
        fill = fill.rstrip()
        fill = fill.split(" ")
        
        for  in range(4):
            if fill 

    
    
        
        
    print(league)
    print(teams)

    print(teams[1].getName())

    

    

main()
    
