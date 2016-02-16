
class Student:
    def __init__(self, id, name, group):
        '''
        Creats a Student instance
        '''
        self.__id=id
        self.__name=name
        self.__group=group
        
    def getId(self):
        '''
        Getter for id.
        '''
        return self.__id
        
    def getName(self):
        '''
        Getter for name.
        '''
        return self.__name
    
    def getGroup(self):
        '''
        Getter for group.
        '''
        return self.__group
    
    def __str__(self):
        '''
        Returns a student as a string.
        '''
        return str(self.__id)+ ';' + str(self.__name) + ';' +str(self.__group)
    
