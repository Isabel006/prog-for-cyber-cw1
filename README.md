# Task 4 – Security Incident Manager

Student 

- Name: Isabel Laura Ndove
- Campus: Lanarkshire
- Banner ID: B01860392

Overview

This project is a Python Security Incident Manager that uses a dictionary to store and manage information about a security incident.

The program demonstrates how dictionaries can be created, accessed, updated and modified using Python.

Features

The program performs the following operations:

1. Create a dictionary: Stores the username, IP address, event type and risk level.
2. Display information: Displays the username and IP address.
3. Add a field: Adds a new field called `status` to show the progress of the incident.
4. Update information: Changes the risk level from `High` to `Critical`.
5. Remove a field: Removes the `event_type` field from the dictionary.
6. Display dictionary contents: Uses a loop to display all remaining keys and values.
7. Count entries: Uses `len()` to calculate the total number of key-value pairs.

Technologies Used

- Python 3
- Python dictionaries
- VS Code

How to Run the Program

1. Open the project folder in VS Code or a terminal.
2. Make sure Python 3 is installed.
3. Run the following command:

```bash
python3 security_incident_manager.py
```

4. The program will automatically perform the dictionary operations and display the results.

Example Information

The program starts with the following incident information:

| Field | Value |
|---|---|
| Username | admin |
| IP Address | 192.168.1.25 |
| Event Type | Multiple failed logins |
| Risk Level | High |

After the operations, the remaining dictionary contains:

- Username: admin
- IP Address: 192.168.1.25
- Risk Level: Critical
- Status: Under Investigation

Total number of key-value pairs: 4

Screenshots

The `screenshots` folder contains evidence of the program running, including:

- Initial incident information.
- Dictionary modifications.
- Final dictionary contents and total number of entries.
  
 Notes
This program was developed as part of Coursework 1 for Programming for Cyber Security. Comments are included to explain the main operations and improve code readability.
