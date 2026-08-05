#multiple inheritance is ussed for one child node with different or multiple parent nodes

class Human:
    def __init__(self):
        self.num_name = 1
        self.num_age = 2
    def work(self):
        print("He can work.")
    def manage(self):
        print("He can manage")    

class Male:
    def flirt(self):
        print("he can flirt")
    def work (self):
        print("He can do somethiing")    

class Female(Human,Male):  #calling takes place
    def blush(self):
        print("she can blush")
    #def work(self):
        #print("she can impress")

boy=Female() 

print(boy.num_name) 

