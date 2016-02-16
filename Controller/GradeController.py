from Repository.GradeRepository import *

class GradeController:
    def __init__(self,grepo):
        self.__grepo=grepo
    
    def assignProblem(self,a):
        '''
        Assigns a problem to a student
        Input: a
        Output:a problem statement is assigned to the student
        Exceptions: raises Exception is the student already has a problem statement for this laboratory
        '''
        self.__grepo.assignProblem(a) 
        
    def getARepository(self):
        '''
        Returns a repository
        '''
        return self.__grepo.getAll()
    
    def __str__(self):
        return str(self.__grepo.getAll())
        
    def assignAgroup(self,lab,group,srepo):
        '''
        '''
        self.__grepo.assignAgroup(lab,group,srepo) 
        
    def gradeStudent(self,idS,lab,grade):
        '''
        '''
        self.__grepo.gradeStudent(idS,lab,grade) 
    
    def orderByAverageAGroup(self,group,srepo):
        '''
        '''
        return self.__grepo.orderByAverageAGroup(group,srepo)    
