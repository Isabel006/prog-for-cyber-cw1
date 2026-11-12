Task 5 – Reusable Cyber Security Utilities

Student Details

- Name: Isabel Laura Ndove
- Campus: Lanarkshire
- Banner ID: B01860392

 Overview

This project is a Python-based Cyber Security Utilities program. It demonstrates how to create and use reusable Python modules to perform common cybersecurity tasks.

The project uses two Python files: `security_tools.py`, which contains reusable functions, and `main.py`, which imports and uses these functions.

Features

The program includes the following features:

1. Password Validation: Checks whether a password meets the required length and character variety.
2. IP Address Validation: Checks the format of an IP address, including the number of octets and whether each value is between 0 and 255.
3. Random Password Generation: Generates a strong random password between 10 and 16 characters, containing uppercase letters, lowercase letters, numbers and symbols.
4. Python Module Importing: Uses a separate module to organise and reuse cybersecurity functions.

Project Structure

- `security_tools.py` – Contains the password validation, IP validation and random password generation functions.
- `main.py` – Imports the security tools module, asks the user for input and displays the results.

Technologies Used

- Python 3
- Python modules
- VS Code

 How to Run the Program

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code or a terminal.
3. Make sure both Python files are in the same folder.
4. Run the following command:

```bash
python3 main.py
```

5. Follow the instructions displayed by the program.

 Testing

The program should be tested with:

- Strong and weak passwords.
- Valid and invalid IP addresses.
- Generated passwords to check their length and character variety.

Screenshots

The `screenshots` folder contains evidence of the program running and displaying the validation results and generated passwords.

Assumptions and Limitations
- Passwords must contain at least 10 characters, including at least one letter, one digit and one symbol.
- The IP address validator performs basic IPv4 format validation. It checks for exactly four numeric octets, with each value between 0 and 255. It does not perform additional network or IP address checks.
- Generated passwords have a random length between 10 and 16 characters and include at least one uppercase letter, one lowercase letter, one digit and one symbol.
- The program uses sample inputs provided by the user and does not connect to a real authentication system or network.

Notes
This project was developed as part of Coursework 1 for Programming for Cyber Security. Comments are included to explain the main functions and important operations.
