class Person:
    def __repr__(self,name,age,city):
        return "Person(name={},age={},city={})" .format(self.name,self.age,self.city)
p=Person ("Pravi","22","bynepalli") 
print(p.name,p.age,p.city)