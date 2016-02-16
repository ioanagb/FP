from Domain.Student import *
from Domain.StudentValidator import *
from Domain.Grade import *

class Repository:
    def __init__(self):
        self.__data=[]
        
    def getAll(self):
        '''
        Getter for data
        '''
        return self.__data
        
    def searchById(self,id):
        '''
        Searches for an obj by id.
        Input:id-integer number
        Output:-1-if id does not exist in the list
              i-position, otherwise
        '''
        for i in range (len(self.__data)):
            if id==self.__data[i].getId():
                return i
        return -1 
        
        
    def add(self,obj):
        '''
        Adds an object to the Repository.
        Input:obj-an object
        Output:the obj is added
        '''
        self.getAll().append(obj)
        
    def remove(self,obj):
        '''
        '''
        self.getAll().remove(obj)
        
    def __str__(self):
        r = "Repository:\n"
        for e in self.__data:
            r += str(e)
            r += "\n"
        return r
        
'''def test():
    l=[[1,'ana',1],
       [2,'matei',2]]
    self.searchById(1)'''
        
        
        
        