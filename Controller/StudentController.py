from Repository.StudentRepository import *

class StudentController:
    '''
    Creates a new instance of StudentController
    '''
    def __init__(self,srepo):
        self.__srepo=srepo

    def getStudents(self):
        return self.__srepo.getStudents()
        
    def addStudent(self,s):
        '''
        Adds a student to the repository
        Input:s-object of type student
        Output: s is added
        '''
        self.__srepo.addStudent(s)
        
    def removeStudent(self,id):
        '''
        Removes a student.
        Input: id-natural nr
               grepo- grades repository
        Output:list of student with s delete if there is no grade for it
        '''
        self.__srepo.removeStudent(id)
        
    def getARepository(self):
        '''
        Returns a repository
        '''
        return self.__srepo.getAll()
    
    def __str__(self):
        result = ''
        for student in self.__srepo.getAll():
            result = result + str(student) + '\n'
        return result
