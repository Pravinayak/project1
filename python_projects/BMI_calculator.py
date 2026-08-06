
import bmi_logo 
print(bmi_logo.bmi_calc)
print("BMI CALCULATOR")

weight=int(input("Enter the weight:"))
height=float(input("Enter the height:"))

bmi= weight / height*2 

print(f"BMI is :{bmi} kg/m2")
if bmi >100:
    print('Your overweighted')

else:
    print("Your normal. ")    