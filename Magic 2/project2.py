user_inputs = []

print("Please enter 10 values:")
for i in range(10):
    value = input(f"Enter value {i + 1}: ")
    user_inputs.append(value)

print("\nYou entered:")
for i, value in enumerate(user_inputs, start=1):
    print(f"Value {i}: {value}")