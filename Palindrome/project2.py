
numbers = []


print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


total_sum = sum(numbers)


print(f"\nThe numbers you entered are: {numbers}")
print(f"The sum of the numbers is: {total_sum}")