m=int(input("Enter any number to find the prime"))
for i in range(2,m):
    if m%i==0:
        print("The number you have enter is non prime")
        break
else:
    print("If it is not falling into the non prime category then the number is prime")
    
    