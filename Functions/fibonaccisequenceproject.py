def fibonacci_series(n):
     a, b = 0, 1
     if n <= 0:
           print("Please enter a positive integer.")
     elif n == 1:
        print(a)
     else:
           print("Fibonacci series up to", n, "terms:")
           print(a, b, end=" ")
for _ in range(2, n):
        a, b = b, a + b
        print(b, end=" ")
        print()
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series(n)

