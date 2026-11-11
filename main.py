
# ==========================================
# TASK 5: REUSABLE CYBER SECURITY UTILITIES
# File: main.py
# ==========================================

# Import the module containing reusable cybersecurity functions
import security_tools


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("===================================")
print("       CYBER SECURITY TOOLS")
print("===================================")


# Ask the user to enter a password
password = input("\nEnter a password: ")

# Ask the user to enter an IP address
ip_address = input("Enter an IP address: ")


# ------------------------------------------
# Check Password Strength
# ------------------------------------------

print("\n========== PASSWORD CHECK ==========")

# Call the password validation function
if security_tools.validate_password(password):
    print("Password is valid and meets the security requirements.")

else:
    print("Password is not strong.")
    print("Suggested strong password:")

    # Call the password generator function
    suggested_password = security_tools.generate_password()

    print(suggested_password)
    print("Keep this password secure and do not share it.")


# ------------------------------------------
# Check IP Address
# ------------------------------------------

print("\n========== IP ADDRESS CHECK ==========")

# Call the IP address validation function
if security_tools.validate_ip(ip_address):
    print("The IP address has a valid format.")

else:
    print("Invalid IP address format.")


# ------------------------------------------
# END OF PROGRAM
# ------------------------------------------

print("\nCyber Security Checks Completed.")
