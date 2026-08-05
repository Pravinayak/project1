#without encapsulation
#here withot encapsulation accessing of data takes places from outside can result in modify 
#of the inside (class) data or variables..

class Bank:
    def __init__(self):
        self.money=1000.   #self.money has 1000 but ,, in output we get '0' because the data is been modified outside the class
    def balance(self):
        print(self.money)   
    def deposit(self,amount):
        self.money+=amount     
b=Bank()
b.money=0       #modified ,but the inside data is different ,but we get the balance is "0"
b.balance()