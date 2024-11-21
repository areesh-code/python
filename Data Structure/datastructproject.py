import random
comp=random.randint(1,10)
user=int(input("Enter a number between 1 and 10: "))
if user==comp:
  print("You win!")
  if user <=comp:
    print("Too low and you lose!")