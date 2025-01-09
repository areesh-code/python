N = int(input("Take the largest number: "))
M = int(input("Take the smallest number: "))
a, b = N, M
while M:
    L = M
    M = N % M
    N = L
LCM = (a * b) // N
print(LCM)