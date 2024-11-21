wd = int(input("Enter the working days"))
a=int(input("Enter the absentees"))
result=(a/wd) * 100
print(result)
if result > 25:
    print("You are not allowed to sit")

else:
    print("You are able to sit")
      