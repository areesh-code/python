m=int(input("Enter any smaller number to find the prime"))
n=int(input("Enter any larger number to find the prime"))
for j in range(m,n+1):
    for i in range(2,j):
        if j%i==0:
           break
    else:
        print(j)