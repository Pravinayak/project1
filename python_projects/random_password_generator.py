import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','W','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['1','2','3','4','5','6','7','8','9','0']

symbols=['!','@','#','$','%','&','*']

print("**PASSWORD-GENERATOR**")
n_letters=int(input("\n How many letters u want in your password:"))
n_numbers=int(input("\n How many numbers u want in your password:"))
n_symbols=int(input("\n How many symbols u want in your password:"))

pass_list=[]

for i in range(1,n_letters+1):
    char=random.choice(letters)
    pass_list +=char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    pass_list +=char


for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    pass_list +=char
 

random.shuffle(pass_list)
password=''
for i in pass_list:
    password+=i
print(f"\n THE GENERATED PASSWORD IS :\n \n {password} \n")    







