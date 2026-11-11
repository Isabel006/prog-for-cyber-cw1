
# ==========================================
# SECURITY TOOL
# ==========================================

from datetime import datetime, timedelta


# ------------------------------------------
# Main authentication details
# ------------------------------------------

correct_username = "admin"
correct_password = "Secure123"

max_login_attempts = 3
failed_logins = 0
authentication_successful = False


# ------------------------------------------
# Function 1: Security Event Counter
# ------------------------------------------

def security_event_counter():

    # Store the correct password
    event_password = "Password123"

    # Initialise counters
    correct_count = 0
    incorrect_count = 0

    # Ask for a password 10 times
    for attempt in range(10):

        entered_password = input("Enter password: ")

        # Check if the password is correct
        if entered_password == event_password:
            correct_count = correct_count + 1
            print("Correct password.")

        else:
            incorrect_count = incorrect_count + 1
            print("Incorrect password.")

    # Calculate incorrect password percentage
    incorrect_percentage = (incorrect_count / 10) * 100

    # Display results
    print("\nSecurity Event Counter Results")
    print("Correct passwords:", correct_count)
    print("Incorrect passwords:", incorrect_count)
    print("Incorrect percentage:", incorrect_percentage, "%")

    # Display alert if more than 50% are incorrect
    if incorrect_percentage > 50:
        print("ALERT: More than 50% of passwords were incorrect!")


# ------------------------------------------
# Function 2: Brute-Force Simulation
# ------------------------------------------

def brute_force_simulation():

    # Predefined password
    brute_password = "Cyber123"

    # Maximum number of attempts
    max_attempts = 3
    attempts = 0

    # Track whether the password was found
    password_found = False

    # Allow the user to guess the password
    while attempts < max_attempts:

        guess = input("Guess the password: ")
        attempts = attempts + 1

        if guess == brute_password:
            print("Password found!")
            password_found = True
            break

        else:
            print("Incorrect guess.")

    # Display the final result
    if password_found == False:
        print("Maximum attempts reached. Access denied.")

    print("Total attempts:", attempts)


# ------------------------------------------
# Function 3: Login Authentication
# ------------------------------------------

login_username = "user"
login_password = "User123"

max_attempts = 3
account_frozen_until = None


def login_authentication():

    global account_frozen_until

    # Check whether the account is currently frozen
    if account_frozen_until is not None:

        if datetime.now() < account_frozen_until:
            print("Account frozen for 24 hours.")
            print("Login is currently blocked.")
            return

        else:
            # Reset the frozen status after 24 hours
            account_frozen_until = None

    # Initialise failed login counter
    failed_attempts = 0

    # Allow three failed login attempts
    while failed_attempts < max_attempts:

        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        # Check username and password
        if entered_username == login_username and entered_password == login_password:

            print("Login successful!")
            break

        else:
            failed_attempts = failed_attempts + 1
            print("Login failed.")

    # Freeze the account after three failed attempts
    if failed_attempts == max_attempts:

        account_frozen_until = datetime.now() + timedelta(hours=24)

        print("Account frozen for 24 hours.")
        print("Too many failed login attempts.")


# ------------------------------------------
# MAIN PROGRAM: Initial Authentication
# ------------------------------------------

print("Welcome to the Security Tool")

while failed_logins < max_login_attempts:

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check initial authentication
    if username == correct_username and password == correct_password:

        print("Authentication successful!")
        authentication_successful = True
        break

    else:

        failed_logins = failed_logins + 1

        print("Incorrect username or password.")
        print("Attempts remaining:", max_login_attempts - failed_logins)


# ------------------------------------------
# MAIN MENU
# ------------------------------------------

if authentication_successful == True:

    while True:

        print("\n========== SECURITY MENU ==========")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        # Option 1: Security Event Counter
        if choice == "1":

            security_event_counter()

        # Option 2: Brute-Force Simulation
        elif choice == "2":

            brute_force_simulation()

        # Option 3: Login Authentication
        elif choice == "3":

            login_authentication()

        # Option 4: Exit
        elif choice == "4":

            print("Thank you for using the security tool")
            break

        # Invalid menu option
        else:

            print("Invalid option. Please select 1, 2, 3 or 4.")

else:

    print("Account frozen for 24 hours.")
    print("Program terminated.")
