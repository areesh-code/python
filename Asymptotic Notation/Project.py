def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
    
    j=1
    while(j<=n+1):
        print("Second Loop", j)

        j=j*2
    
    for i in range(0,100):
        print("Third loop")

    def print_time_complexities():
        print("First Loop: O(n)")
    print("Second Loop: O(log n)")
    print("Third Loop: O(1)")
    print("Total Time Complexity: O(n)")

    print_time_complexities()