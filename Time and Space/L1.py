def Fun(n):
    return n*(n+1)/2
print(Fun (8))
# The number iterations will be 1 irrespectieve of the value of n

def Fun2(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(Fun2(8))
# The number iterations will be as per the value of n

def Fun3(n):
    sum=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum=sum+1
    return sum
print(Fun3(8))
# The number of iterations will be 36 as two loops are involved





