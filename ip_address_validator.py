
# ==========================================
# TASK 3: IP ADDRESS VALIDATOR
# ==========================================

# Create a function to validate an IP address
def validate_ip(ip_address):

    # Remove unnecessary spaces from the IP address
    ip_address = ip_address.strip()

    # Check if the IP address contains exactly three dots
    if ip_address.count(".") != 3:
        return False

    # Split the IP address into four separate numbers
    numbers = ip_address.split(".")

    # Check if there are exactly four numbers
    if len(numbers) != 4:
        return False

    # Loop through each octet to check whether it contains a valid number
    for number in numbers:

        # Check if each part contains only digits
        if not number.isdigit():
            return False

        # Convert the number from a string to an integer
        number = int(number)

        # Check if the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    # All checks have passed
    return True


# ==========================================
# MAIN PROGRAM
# ==========================================

# Ask the user to enter an IP address
ip_address = input("Enter an IP address: ")

# Call the function and check the result
if validate_ip(ip_address):

    print("Valid IP address")

else:

    print("Invalid IP address")
