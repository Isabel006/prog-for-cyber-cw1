# Security Tool

## Overview

This project is a Python-based Security Tool that demonstrates basic cybersecurity concepts, including password checking, brute-force simulation and login authentication.

The program requires the user to authenticate before accessing the security menu. It provides three security features and an option to exit.

## Features

### 1. Initial Authentication
- Requires a username and password before accessing the program.
- Allows a maximum of three login attempts.
- Terminates the program after three unsuccessful attempts.

### 2. Security Event Counter
- Requests a password ten times.
- Counts the number of correct and incorrect passwords.
- Calculates the percentage of incorrect passwords.
- Displays a security alert if more than 50% of passwords are incorrect.

### 3. Brute-Force Simulation
- Simulates attempts to guess a predefined password.
- Allows a maximum of three attempts.
- Displays a success message if the correct password is entered.
- Displays an access-denied message if all attempts are unsuccessful.

### 4. Login Authentication
- Checks a predefined username and password.
- Allows up to three failed login attempts.
- Freezes the account for 24 hours after three unsuccessful attempts.
- Prevents further login attempts while the account is frozen.

### 5. Exit
- Allows the user to close the program.
- Displays the message: "Thank you for using the security tool".

## Requirements

- Python 3
- VS Code or another Python editor

## How to Run the Program

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python3 security_tool.py
```

5. Enter the initial authentication credentials when requested.

## Test Credentials

| Feature | Username | Password |
|---|---|---|
| Initial Authentication | admin | Secure123 |
| Login Authentication | user | User123 |
| Security Event Counter | Not required | Password123 |
| Brute-Force Simulation | Not required | Cyber123 |

## Notes

The account freeze is simulated using Python's date and time functionality. The frozen status is held in memory and resets when the program is restarted.

The predefined passwords are for coursework demonstration purposes only and should not be used for real accounts.
