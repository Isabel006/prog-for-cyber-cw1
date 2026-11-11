
# ==========================================
# TASK 5: REUSABLE CYBER SECURITY UTILITIES
# File: security_tools.py
# ==========================================

import secrets
import string


# ------------------------------------------
# Function 1: Password Validator
# ------------------------------------------

def validate_password(password):

    # Check if the password has at least 10 characters
    if len(password) < 10:
        return False

    # Check if the password contains at least one letter
    has_letter = any(char.isalpha() for char in password)

    # Check if the password contains at least one digit
    has_digit = any(char.isdigit() for char in password)

    # Check if the password contains at least one symbol
    has_symbol = any(char in string.punctuation for char in password)

    # Return True only if all requirements are met
    return has_letter and has_digit and has_symbol


# ------------------------------------------
# Function 2: IP Address Validator
# ------------------------------------------

def validate_ip(ip_address):

    # Remove unnecessary spaces
    ip_address = ip_address.strip()

    # Check if the IP address contains exactly three dots
    if ip_address.count(".") != 3:
        return False

    # Split the IP address into four octets
    numbers = ip_address.split(".")

    # Check if there are exactly four octets
    if len(numbers) != 4:
        return False

    # Check that every octet is numeric and within the valid range
    for number in numbers:

        # Check if the octet contains digits only
        if not number.isdigit():
            return False

        # Convert the octet into an integer
        number = int(number)

        # Check if the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    # All IP address checks have passed
    return True


# ------------------------------------------
# Function 3: Strong Password Generator
# ------------------------------------------

def generate_password():

    # Define the characters used to generate passwords
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all available characters
    all_characters = uppercase + lowercase + digits + symbols

    # Generate a secure random password length between 10 and 16
    password_length = secrets.randbelow(7) + 10

    # Guarantee at least one character from each required category
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the remaining positions with random characters
    for attempt in range(password_length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle the characters to make their order unpredictable
    secrets.SystemRandom().shuffle(password)

    # Join the characters into one password string
    strong_password = "".join(password)

    # Return the generated password
    return strong_password
