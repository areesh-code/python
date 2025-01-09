N=int(input("Take the largest number"))
M=int(input("Take the smallest number"))
while M:
    L=M
    M=N%M
    N=L
print(N)
