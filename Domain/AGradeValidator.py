from Domain.Grade import *

class AGradeValidator:
    
    @staticmethod
    def validateGrade(grade):
        '''
        Validates the grade of a student at a laboratory
        '''
        errmsj=""
        if grade()<0:
            errmsj="Grade can not be negative!"
        if grade()>10:
            errmsj="Grade can not be greater than 10!"
        if errmsj!="":
            raise Exception(errmsj)