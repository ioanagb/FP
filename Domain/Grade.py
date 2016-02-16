
class Grade:
    
    def __init__(self, idS, labNr, prbNr, grade):
        '''
        Creates an instance of type Grade.
        '''
        self.__idS=idS
        self.__idL=labNr
        self.__prbNr=prbNr
        self.__grade=grade
        
        
    def getIdS(self):
        '''
        Getter for idS.
        '''
        return self.__idS
    
    def getPrbNr(self):
        '''
        Getter for prbNr
        '''
        return self.__prbNr
    
    def getGrade(self):
        '''
        Getter for grade.
        '''
        return self.__grade
    
    def getLabNr(self):
        '''
        Getter for idL
        '''
        return self.__idL
    
    def setGradee(self,grade):
        '''
        '''
        self.__grade=grade
    
    