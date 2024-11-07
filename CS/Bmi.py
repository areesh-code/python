h=float(input("Enter Height in cm"))
w=float(input("Enter weight in kg's"))
BMI=w/(h/100)**2
print (BMI)
if BMI<= 18.4:
    print("You are under weight") 
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are over weight")
elif BMI <= 34.9:
    print("You are severaly over weight")
elif BMI <= 39.9:
    print("You are obeses") 
else:
    print("You are severely obese")  