
''' for private data 2 underscores nd for protected 1 underscore'''


class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary#private data

    def get_salary(self):#public data
         print(self.__salary)

    def Empdisplay(self):#public method
        print(self.name,self.role)
        
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):#protected method
        print('hiring for the manager role')


cobj=Company('ms','hyd')
eobj=Employee('akhila','trainer',90000)
eobj.Empdisplay()
cobj._hiring()
    
