N=int(input("Enter the number of your choice"))
temp=N
sum=0
while temp >0:
    r=temp%10
    sum=sum+r**3
    temp=temp//10
if N == sum:
    print("The answer is armstrong")
else:
    print("The value of number is not armstrong")
