import os
def add (a,b):
    return a + b
def sub (a,b):
    return a - b
def multiply (a,b):
    return a * b
def divide (a,b):
    return a / b

opt_dict= {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
def calculator():

    num1= int(input("Enter the first number:"))
    cont=True
    for symbol in opt_dict:
        print(symbol)

    while cont==True :

        op_symbol=input("Pick operation:")   
        num2= int(input("Enter the second number:"))  
        calculator_function=opt_dict[op_symbol] 
        output=calculator_function(num1,num2)

        print(f"{num1} {op_symbol} = {num2}={output}")

        another= input(f" Press 'y' to continue with {output} , or\n 'n' for new calculations ,or\n 'x' to Exit.... ").lower()
        if another== 'y':
            num1=output
        elif another=='n':

            cont=False
            os.system('cls')
            calculator()
        else:
            cont=False
            print("BYE")    
calculator()            






