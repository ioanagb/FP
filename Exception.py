
class Exception(Exception):
    def __init__(self,msj):
        self.__msj=msj
        
    def __str__(self):
        return str(self.__msj)