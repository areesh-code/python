def is_armstrong_number(number):
     num_str = str(number)
     num_digits = len(num_str) 
     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
     return sum_of_powers == number
user_input = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
