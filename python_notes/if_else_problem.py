total_amount=10000
withdraw_limit=5000

withdraw= int(input("Enter the amount:"))
atm_pin=True
account_active= True

if not account_active :
    print("Account is temporary out of service")
else:
    print("Transaction is going on.....")

    if not atm_pin:
        print("Wrong credentails")
    else:
        print("you have entered correct password")

    if withdraw> total_amount:
        print("Insufficient balance.")
        print(f"current balance is:{total_amount}")
    elif withdraw>withdraw_limit:
        print("Daily limit reached")
        print(f"you can collect upto {withdraw_limit}")
    elif withdraw <0:
        print("Invalid amount......")
    else :
        total_amount-= withdraw
        print("Dispensing cash")
        print("Remaining balance:",total_amount)
print("Session completed")