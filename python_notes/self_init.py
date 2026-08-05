#__init__ is also called as the constructor
#__init__ automatically runs when object is created without calling function
#self is used to store data in object


class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print(self.name,self.color)
c1=car("bmw","white")    
c2=car("audi","red")    #multiple objects



class Man:
    def __init__(self,run,walk):
        self.run=run
        self.walk=walk
        print(self.run,self.walk)
h=Man("walking","Runnning")        
