#with encapsulation
#It provides security the class ,and protects the data in the class
#It allows the data to modify in class methods,not directly through outside
#It helps data safe and secure

class Bank:
    def __init__(self):
        self.__money=1000   #we added '__' to the variable for making "PRIVATE"
    def balance(self):
        print(self.__money)   
    def deposit(self,amount):
        self.__money+=amount     
b=Bank()
b.deposit(3000)
b.__money=0 #if we modify from outside ,it wont change the class inside data
b.balance()
   