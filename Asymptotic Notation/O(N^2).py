def Square(N):
    iteration=0
    for i in range(0, N):
        for j in range(0,N): 
            print("*", end="")
            iteration=iteration+1
        print("")
    print("the total iteration is", iteration, "The value of N was this", N)

Square(5)
Square(4)
Square(3)

print("O(N^2) is time complexcity")

        
