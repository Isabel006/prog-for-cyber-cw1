# Task 2 – Security Event Logger

Name: Isabel Laura Ndove
Campus: Lanarkshire
Banner ID: B01860392

1. Overview

The Security Event Logger is a Python program that records login attempts. It asks the user to enter a username and password until the correct login details are provided.

The program records both failed and successful login attempts and displays an event log for each attempt.

2. Features

The program includes the following features:

- Requests a username and password from the user.
- Checks whether the entered login details are correct.
- Records failed login attempts.
- Records successful login attempts.
- Generates a unique Event ID for each login attempt.
- Displays the username used during the attempt.
- Records an IP address.
- Records the date and time of each attempt.

3. Event Log Information

Each event log displays:

| Field | Description |
|---|---|
| Event ID | A unique number for each login attempt |
| Username | The username entered by the user |
| IP Address | The IP address recorded for the attempt |
| Event | Whether the login was successful or failed |
| Timestamp | The date and time of the attempt |

4. Requirements

- Python 3
- Visual Studio Code or another Python editor

5. How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Navigate to the project folder.
4. Run the following command:

`python3 security_event_logger.py`

6. Testing

The program should be tested using:

- Incorrect username and password.
- Correct username and password.
- Multiple failed login attempts followed by a successful login.

Screenshots showing the program's output are saved in the `screenshots` folder.
