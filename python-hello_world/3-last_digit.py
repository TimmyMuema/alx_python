import random

number = random.randint(-10000, 10000)

last_digit = number % 10

sign = 'is positive' if number >= 0 else 'is negative'

message = 'and is greater than 5' if last_digit > 5 else \
    'and is 0' if last_digit == 0 else \
    'and is less than 6 and not 0'

print(f"Last digit of {number} {sign} {last_digit} {message}")

