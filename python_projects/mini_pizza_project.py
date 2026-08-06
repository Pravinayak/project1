size= input("enter size of pizza S/M/L:")
bill=0

if size=='s' or size=="S" :
    bill+=100
    print("small pizza is 100")
elif size=="m" or size=="M" :
    bill+=200
    print("Medium pizza is 200")
else :
    bill+=300
    print("Large pizza is 300")

sause=input("want some sauce:Y/N")
if sause=="y" or   sause=="Y":
    bill+=30
else:
    bill+=50

chilli_flakes=input("want some chilli flakes:Y/N")
if chilli_flakes=="y" or chilli_flakes =="Y":
    bill+=20
print(f"your total bill is :{bill}")                    

