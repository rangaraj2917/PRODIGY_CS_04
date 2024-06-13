def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Assessing strength based on criteria
    if length < 8:
        strength = "Weak"
    elif 8 <= length <= 12 and (has_upper + has_lower + has_digit + has_special >= 3):
        strength = "Moderate"
    elif length > 12 and (has_upper + has_lower + has_digit + has_special >= 3):
        strength = "Strong"
    else:
        strength = "Weak"  # This case is unlikely due to previous conditions

    return strength

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")

