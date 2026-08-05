#Inheritance allows a child class to use the properties and methods
#It helps code reuse and reduce the duplicate
#Easyy to maintain
#parent node - parent , super ,base
#child node- child,sub,diverse

class Employe:
    def __init__(self):
        self.eyes=2
        self.nose=1
    def work(self):
        print("Employe is working...")

class Developer(Employe):  #Inheritance can be inserted in the class braackets 
    def code(self):
        print("Developer is developing..")

class Tester(Employe):
    def test(self):
        print("Tester is testing..")
    def work(self):         #Actually method overridding takes place .
        super().work()
        print("analysing...")    

t=Tester()
t.work()    
print(t.eyes)
