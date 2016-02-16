from Controller.StudentController import *
from Controller.GradeController import *

class UI:
    def __init__(self,sctrl,gctrl):
        self.__sctrl=sctrl
        self.__gctrl=gctrl
        
    def readPosInteger(self,msj):
        '''
        Reads a positive integer.'''
        res=0
        while True:
            try:
                res=int(input(msj))
                if res<0:
                    raise ValueError
                break
            except ValueError:
                print("The value you introduced was NOT a positive integer.")
        return res
           
    def __addStudent(self):
        '''
        Adds a student to the list
        Input:-
        Output: s is added to the repository
        '''
        id=self.readPosInteger("Please enter an id.\n")
        name=input("Please enter a name.\n")
        group=self.readPosInteger("Please enter group number.\n")
        s=Student(id, name,group)
        try:
            #s=Student(id, name,group)
            StudentValidator.studValidate(self, s)
            self.__sctrl.addStudent(s)
        except Exception as e:
            print(e)
            
    def __removeStudent(self):
        '''
        Removes a student.
        Input: -
        Output:list of student with s delete if there is no grade for it
        '''
        id=self.readPosInteger("Please enter an id.")
        name=input("Please enter a name.\n")
        group=self.readPosInteger("Please enter group number.\n")
        s=Student(id, name,group)
        try:
            self.__sctrl.removeStudent(s)
        except Exception as e:
            print(e)
            
    def __assignProblem(self):
        '''
        Assigns a problem to a student
        Input: 
        Output:a problem statement is assigned to the student
        Exceptions: raises Exception is the student already has a problem statement for this laboratory
        '''
        idS=self.readPosInteger("Please enter an id.")
        labNr=self.readPosInteger("Please enter lab nr. \n")
        flag=True
        while flag:
            prbNr=self.readPosInteger("Please enter problem number.\n")
            if prbNr>=1 or prbNr<=20:
                flag=False 
            else:
                print("The problem number should lie between 1 and 20!")
        try:
            g=Grade(idS,labNr,prbNr,0)
            self.__gctrl.assignProblem(g)
        except Exception as e:
            print(e)
            
    def __assignAgroup(self):
        '''
        '''
        lab=self.readPosInteger("Please enter laboratory number. ")               
        group=self.readPosInteger("Please enter group number. ")
        self.__gctrl.assignAgroup(lab,group,self.__sctrl)
        
    def __gradeStudent(self):
        '''
        '''
        idS=self.readPosInteger("Please enter an id.")
        lab=self.readPosInteger("Please enter laboratory number. ")
        grade=lab=self.readPosInteger("Please enter a grade. ")
        try:
            AGradeValidator.validateGrade(grade)
            self.__gctrl.gradeStudent(idS,lab,grade)
        except Exception as e:
            print(e)    
        
    def __orderByAverageAGroup(self):
        '''
        '''
        group=self.readPosInteger("Please enter group number. ")
        l=[]
        l=self.__gctrl.orderByAverageAGroup(group,self.__sctrl)
        for el in l:
            print(el)
               
    def mainMenu(self):
        '''
        Prints the main menu.
        '''
        while True:
            print('Available Commands: \n 0-exit\n 1-add student\n 2-remove student\n 3-assign a problem to a student\n 4-assign a group \n 5-grade a student \n 6-print a group ordered by average \n')           
            command=input('Please enter a command.\n')
            
            if command=='0':
                print('Bye')
                return
            elif command=='1':
                self.__addStudent()
            elif command=='2':
                self.__removeStudent()
            elif command=='3':
                self.__assignProblem()
            elif command=='4':
                self.__assignAgroup()
            elif command=='5':
                self.__gradeStudent()
            elif command=='6':
                self.__orderByAverageAGroup()
            else:
                print("Invalid command!")
        
        
        