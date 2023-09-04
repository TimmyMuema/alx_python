def validate_password(password):
    length_validator = len(password) >= 8
    upper_validator = any(char.isupper() for char in password)
    lower_validator = any(char.islower() for char in password)
    digit_validator = any(char.isdigit() for char in password)
    space_validator = not any(char.isspace() for char in password)
    return length_validator and upper_validator and lower_validator and digit_validator and space_validator

