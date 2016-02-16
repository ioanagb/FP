from Repository.Repository import *
from Domain.AGradeValidator import *
from OrderByAverageAGroup import OrderByAverageAGroup

class GradeRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename=filename
        self.__loadFromFile()
        
    def __loadFromFile(self):
        '''
        Loads grades from file.
        Input:-
        Output:the grades which are in the file are stored into MemoryError
        '''
        
        try:
            f=open(self.__filename,"r")
        except IOError:
            return
        
        for line in f:
            line=line.strip()
            gradeAtrib=line.split(";")
            
            if len(gradeAtrib)!=4:
                continue
            
            idS=int(gradeAtrib[0].strip())
            idL=int(gradeAtrib[1].strip())
            prbNr=int(gradeAtrib[2].strip())
            grade=int(gradeAtrib[3].strip()) 
            
            grd=Grade(idS,idL,prbNr,grade) 
            
            Repository.add(self, grd)  
        f.close()
            
    def __saveToFile(self):
        '''
        Saves to file data
        Input:-
        Output:the grades are saved from memory into file
        '''
        f=open(self.__filename,"w")
        for g in Repository.getAll(self):
            f.write(str(g.getIdS()) + ';' + str(g.getLabNr()) + ';' + str(g.getPrbNr()) + ';' + str(g.getGrade()) + '\n')
        f.close()            
        
    def searchIdAndLab(self, idS, labNr):  
        '''
        '''
        for g in Repository.getAll(self):
            if g.getIdS()==idS and g.getLabNr()==labNr:
                return True
        return False  
        
    def assignProblem(self,a):
        '''
        Assigns a problem to a student
        Input: idS-integer, student id
                labNr-integer, laboratory number
                prbNr-integer, problem number
        Output:a problem statement is assigned to the student
        Exceptions: raises Exception is the student already has a problem statement for this laboratory
        '''
        if self.searchIdAndLab(a.getIdS(), a.getLabNr())==True:
            raise Exception("The student already has a problem statement for this laboratory")
        Repository.add(self, a)
        self.__saveToFile()

    def assignAgroup(self,lab,group,srepo):
        '''
        iau fiecare student din repository si daca e din grupul meu adaug o problema pentru el (daca nu se afla deja in repositoriul de gardes) 
        '''
        prbNr=1
        for s in srepo.getStudents():
            if prbNr >= 21:
                prbNr = 1
            
            print(type(s.getGroup()), type(group), s.getId(), lab, self.searchIdAndLab(s.getId(), lab) == False)
            if (int(s.getGroup()) == group) and (self.searchIdAndLab(s.getId(), lab) == False):
                print('HERE')
                g=Grade(s.getId(), lab, prbNr,0)
                self.assignProblem(g)
                prbNr+=1

    
    def gradeStudent(self,idS,lab,grade):
        '''
        '''
        flag=0
        for el in self.getStudents():
            if idS==el.getIdS() and lab == el.getLabNr():
                el.setGrade(grade)
                flag=1
                break
        if flag==0:
            raise Exception("There is no assignemnt with this details!")      
        
    def computeAverageForAStudent(self,id):
        '''
        '''
        c=0
        s=0
        for el in self.getAll():
            if el.getIdS()==id:
                s=s+el.getGrade()
                c+=1
        if c!=0:
            return s/c
        else:
            return 0
        
    def orderByAverageAGroup(self,group,srepo):
        '''
        '''
        l=[]
        for s in srepo.getARepository():
            el=OrderByAverageAGroup(s.getName(), self.computeAverageForAStudent(s.getId()))
            l.append(el)            
        l.sort()
        return l
                
        
                    
                    
                    
                    
                    
        
