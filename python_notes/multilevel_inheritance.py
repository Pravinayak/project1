#multi-level inheritance is the deriving the objects from parent nodes- 1(parent node) - 2(child node)- for third class (2 node is parent node)
class Human:
    def __init__(self):
        self.heart=1
    def see(self):
        print("Human can see..")
    def work(self):
        print("Human can work")

class Male(Human):
    def flirt(self):
        print("Male can flirt")      
    def work(self):
        print("MAle can work")
        super().work()  

class Female(Male):
    def blush(self):
        print("She can blush.")

f=Female()
f.work()
f.flirt()

