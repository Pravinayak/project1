import random
import logo_art
easy_attempts=10
hard_attempts=5  
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return easy_attempts
    else:
        return hard_attempts

def check_number(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your Guess is low..")
        return attempts-1
    elif guessed_number>answer:
        print("Your Guess is High") 
        return attempts-1
    else:
        print(f"Yes your guess is absoultely right .\nThe answer is {answer} .")       
def game():
    print(logo_art.logo)
    print("THINKING THE NUMBER FROM '1' TO '50' ....")

    answer=random.randint(1,50)
    print(answer)
    level=input("Enter the level of difficulty 'Easy' or 'Hard'- ")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f" You have {attempts} remaining to guess number...")
        guessed_number=int(input("Guess the number..."))
        attempts=check_number(guessed_number,answer,attempts)
        if attempts==0:
            print("Your out of Guesses..YOU LOSE...")
            return
        elif guessed_number!=answer:
            print("Guess again")
game()    