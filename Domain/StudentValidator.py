from Domain.Student import *

class StudentValidator:
    @staticmethod
    def studValidate(self,s):
        '''
        Validates a student.
        Input:s-object of type student
        Output:-
        Exception: raises Exception if id is not integer
        '''
        errmsj=""   
        if s.getName()=="":
            errmsj += "The name can not be empty"
        if str(s.getGroup())=="":
            errmsj +="The group can not be empty"
        if errmsj!="":
            raise Exception(errmsj)
            
'''def testStudValidate():
    s1=Student(1;'ana';2)
    s2=Student(2;;2)
    assert StudentValidator.studValidate(s1)==""
    assert StudentValidator.studValidate(s2)=="The name can not be empty"
    '''