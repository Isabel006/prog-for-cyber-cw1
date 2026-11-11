
# ==========================================
# TASK 2: SECURITY EVENT LOGGER
# ==========================================

from datetime import datetime

# Store the correct login details
correct_username = "admin"
correct_password = "Secure123"

# Store a sample IP address for the security event logs
# This is not the actual IP address of the person running the program
ip_address = "192.168.1.25"

# Set the starting Event ID
event_id = 3971

print("Welcome to the Security Event Logger")
print("------------------------------------")

# Keep asking for login details until the correct credentials are entered
while True:

    # Ask the user for their username and password
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    # Get the current date and time for the event log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check whether the username and password are correct
    if username == correct_username and password == correct_password:

        event = "Successful login"

    else:

        event = "Failed login"

    # Display the security event log
    print("\n========== SECURITY EVENT LOG ==========")
    print("Event ID:", event_id)
    print("Username:", username)
    print("IP Address:", ip_address)
    print("Event:", event)
    print("Timestamp:", timestamp)
    print("========================================")

    # Increase the Event ID so each login attempt receives a different ID
    event_id = event_id + 1

    # Stop the loop when the correct credentials are entered
    if event == "Successful login":

        print("\nLogin successful! Welcome to the system.")
        break
