class Expression:
    def __init__(self, num1, num2, num3):
         self.num1 = num1
         self.num2 = num2
         self.num3 = num3
    def add(self):
        result = self.num1 + self.num2 + self.num3
        return result
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
expression_obj = Expression(num1, num2, num3)
result = expression_obj.add()
print(f"The result of adding {num1}, {num2}, and {num3} is: {result}")
         
         
         
         
         
         
       