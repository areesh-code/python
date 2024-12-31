def multiply_one_iteration(n, m):
    
    return n * m

def multiply_n_iterations(n, m):
   
    result = 0
    for _ in range(abs(n)):  
        result += m
 
    if n < 0:
        result = -result
    return result


n = int(input("Enter the first number (N): "))
m = int(input("Enter the second number (M): "))


print("Multiplication using one iteration:", multiply_one_iteration(n, m))
print("Multiplication using N iterations:", multiply_n_iterations(n, m))