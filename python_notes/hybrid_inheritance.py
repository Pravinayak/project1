#Hybrid inheritance is the combination of two or more inheritance

class A:
    def display(self):
        print("I am from Class A")
class B(A):
    def display(self):
        print("I am from Class B")

class C:
    def display(self):
        print("I am from Class C")        

class D(B,C):
    def display(self):
        print("I am from Class D")   

d=D()
d.display()            
