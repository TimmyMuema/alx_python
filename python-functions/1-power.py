def pow(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise TypeError('The arguments must be integers or floats')
    return a ** b
