
class OrderByAverageAGroup:
    def __init__(self,name,average):
        '''
        '''
        self.__name=name
        self.__average=average
        
    def __lt__(self,average):
        '''
        '''
        if self.__average>average:
            return False
        else:
            return True
    
    def __str__(self):
        '''
        '''
        return str(self.__name) + ' ' + str(self.__average) 
    