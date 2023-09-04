def is_prime(number):
    return not any(number % i == 0 for i in range(2, int(number ** 0.5) + 1))
