import random

names= input("enter the names separated by commas:")
names_list= names.split(",")
#name_length=len(names_list)
#random_choice=random.randint(0,name_length-1)
print(f"{random.choice(names_list)} will pay the bill.")