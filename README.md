# Task 3 – IP Address Validator

Name: Isabel Laura Ndove
Campus: Lanarkshire
Banner ID: B01860392

1. Overview

The IP Address Validator is a Python program that checks whether an IPv4 address follows the required format.

The program uses a function called `validate_ip()` to check the IP address and determine whether it is valid or invalid.

2. Features

The program includes the following features:

- Accepts an IP address as input.
- Removes unnecessary spaces from the beginning and end of the address.
- Checks that the IP address contains exactly three dots.
- Checks that the address contains four numbers (octets).
- Checks that each octet is between 0 and 255.
- Returns `True` for a valid address or `False` for an invalid address.

3. Example Inputs

| IP Address | Expected Result |
|---|---|
| 192.168.1.25 | True |
| 10.0.0.1 | True |
| 256.168.1.1 | False |
| 192.168.1 | False |
| 192.168.1.1.5 | False |

4. Requirements

- Python 3
- Visual Studio Code or another Python editor

5. How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Navigate to the project folder.
4. Run the following command:

`python3 ip_address_validator.py`

6. Testing

The program should be tested using valid and invalid IP addresses, including addresses with missing octets, extra dots and numbers outside the range of 0–255.

Screenshots showing the program's output are saved in the `screenshots` folder.
