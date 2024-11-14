def squared(N):
    f=1
    for i in range(1,N+1):
        f = f*i
    print(f)
n=int(input("Enter the number"))
squared(n)