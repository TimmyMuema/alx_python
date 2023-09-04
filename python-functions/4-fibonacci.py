def fibonacci_sequence(n):
    a, b = 0, 1
    if n <= 0:
        return []

    fibonacci_numbers = []
    for i in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers
