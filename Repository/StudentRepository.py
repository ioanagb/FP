from Domain.Student import *
from Repository.Repository import *

class StudentRepository(Repository):
    def __init__(self,filename,grepo):
        Repository.__init__(self)
        self.__filename=filename
        self.__grepo=grepo
        self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        Reads data from file.
        Input:-
        Output: the data from file is stored into memory.
        Raises IOError if the file can not be open
        '''
        
        try:
            f=open(self.__filename, "r")
        except IOError:
            return 
        
        for line in f:
            line=line.strip() 
            studAtrib=line.split(";")
            
            if len(studAtrib)!=3:
                continue
            
            studId=int(studAtrib[0].strip())
            studName=studAtrib[1].strip
            studGroup=studAtrib[2].strip()
            
            student=Student(studId,studName,studGroup)
            
            Repository.add(self,student)
            
        f.close()
        
    def __saveToFile(self):
        '''
        Saves students to file.
        Input:-
        Output: adds to file all the students from repository
        '''
        
        f=open(self.__filename,"w")
        for s in self.getAll():
            f.write(str(s.getId()) + ';' +s.getName() + ';' + str(s.getGroup()))
        f.close()
        
    def addStudent(self,s):
        '''
        Adds a student to the repository
        Input:s-object of type student
        Output: s is added to the repository
        '''
        if Repository.searchById(self, s.getId())!=-1:
            raise Exception("The given id already exists!")           
        Repository.add(self, s)
        self.__saveToFile()
        
    def removeStudent(self,obj):
        '''
        Removes a student.
        Input: id-natural nr
               grepo- grades repository
        Output:list of student with s delete if there is no grade for it
        '''
        exists=False
        for g in self.__grepo.getAll():
            if obj.getId()==g.getIdS():
                raise Exception("You can not remove this student because he has grades.")
        if Repository.searchById(self, obj.getId())==-1:
            raise Exception("This student does not exist!")
        
        Repository.remove(self, obj)
        self.__saveToFile()
            
            
            
        
        
                
        
    