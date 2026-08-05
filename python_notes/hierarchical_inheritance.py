#hierarchical inheritance refers to one parent node and multiple child classes

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} , {self.age}")
    def speak(self):
        print("Human can speak.")

class Male(Human):
    def flirt(self):
        print("He can flirt")

class Female(Human):
    def blush(self):
        print("She can blush")

f=Female("Praavi",22)
f.speak()        