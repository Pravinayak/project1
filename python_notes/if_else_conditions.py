a=10
b=20

if a==10:
    print("Welcome to the train!")
    # Inner condition evaluated only if outer condition is True
    if b==20:
        print("Please step away from the boarding line.")
else:
    print("Please purchase a ticket first.")


n=9
result="even" if n%2==0 else "odd"
print(f"the number is {result}")    
