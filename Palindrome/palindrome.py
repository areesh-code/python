N=int(input("Enter the number"))
B=N
M=0
while N >0:
    R=N%10
    M=M*10+R
    N=N//10
if B==M:
    print("The number is Palindrome")
else:
    print("The number is not Palindrome" )
