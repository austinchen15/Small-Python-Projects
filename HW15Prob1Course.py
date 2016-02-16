from HW15Prob1Student import *

class Course:
    def __init__(self,name,dept,cap):
        """ Initializes Course object with a name, department, and class number cap """
        self.name = name
        self.dept = dept
        self.cap = cap
        self.roster = []

    def getCourseName(self):
        """ Returns course name """
        return self.name

    def getCap(self):
        """ Returns the maximum number of students in one class """
        return self.cap

    def getDepartment(self):
        """ Returns the department's name""" 
        return self.dept

    def courseCheck(self):
        """ checks to see if there is room left in the course. If so, it returns true. If not, it's fale """
        if len(self.roster) < self.cap:
            return True
        elif len(self.roster) >= self.cap:
            return False

    def addStudent(self,student):
        """ Adds a student object to the course """
        self.roster.append(student)

    def Print(self):
        """ Returns the class roster """
        print(self.name+":")
        for i in self.roster:
            print(i.getFName()+ " " + i.getLName())

    def __str__(self):
        """ Returns a string that represents the object """
        return self.name
