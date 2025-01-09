def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)  
    except ValueError:
        print("Invalid binary input. Please enter only 0's and 1's.")

while True:
    binary_input = input("Enter your Binary (or type 'exit' to quit): ")
    if binary_input.lower() == 'exit':
        print("Goodbye!")
        break
    binary_to_decimal(binary_input)