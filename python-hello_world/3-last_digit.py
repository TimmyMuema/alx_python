import random

number = random.randint(-10000, 10000)

last_digit = number % 10

sign = "is"
if number < 0:
    last_digit = -last_digit
    sign = "is negative and"

print(f"The last digit of {number} {sign} {last_digit}")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 but not 0")
