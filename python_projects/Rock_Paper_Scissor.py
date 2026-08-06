import random

print("<<<<<------ROCK ,PAPER , SCISSOR------->>>>>>")

user=int(input("Enter your choice as 0- Rock , 1- Paper , 2- Scissor :"))

if user >= 3 or user<0:
    print("Invalid..! YOU LOSE..")

else:
    computer=random.randint(0,2)
    print("Computer picked:")

    if computer==user :
        print("Its a DRAW")
    elif computer==0 and user==2:
        print("YOU LOSE")
    elif user==0 and computer==2:
        print("YOU WIN")
    elif user>computer :
        print("YOU WIN")
    elif computer>user :
        print("YOU LOSE")                    
