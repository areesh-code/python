t = (0, 1, 1, 0, 1)

count_zeros = 0
count_ones = 0

for num in t:
    if num == 0:
        count_zeros += 1
    elif num == 1:
        count_ones += 1

if count_ones > count_zeros:
    weather = "Rainy"
else:
    weather = "Sunny"

print(f"Count of 0s: {count_zeros}")
print(f"Count of 1s: {count_ones}")
print(f"The predicted weather is: {weather}")





